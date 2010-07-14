import re
import logging
import traceback
from paste import request
import arecibo
from weberror.errormiddleware import ErrorMiddleware

log = logging.getLogger(__name__)

IPV4_ADDRESS =  re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

def remote_address(environ):
    proxies=environ.get("HTTP_X_FORWARDED_FOR", None)
    if proxies is not None:
        proxies=proxies.replace(" ", "")
        addresses=[a for a in proxies.split(",") if IPV4_ADDRESS.match(a)]
        if addresses:
            return addresses[0]

    return environ.get("REMOTE_ADDR", None)



class AreciboMiddleware(ErrorMiddleware):
    """WSGI middleware to report any errors to an Arecibo server.
    """

    def __init__(self, app, global_conf=None, url=None, account=None):
        self.application = app
        if global_conf is None:
            global_conf = {}

        if url is not None:
            self.url = url
        else:
            self.url = global_conf.get("url")

        if account is not None:
            self.account = account
        else:
            self.account = global_conf.get("account")


    def report(self, exc_info, environ):
        report = arecibo.post()
        report.server(url=self.url)
        report.set("account", self.account)
        report.set("status", "500")
        report.set("url", request.construct_url(environ))
        report.set("user_agent", environ.get("HTTP_USER_AGENT"))
        report.set("ip", remote_address(environ))
        report.set("type", exc_info[0].__name__)
        report.set("traceback", traceback.format_exc(exc_info[2]))
        report.send()


    def exception_handler(self, exc_info, environ):
        try:
            self.report(exc_info, environ)
        except:
            log.exception("Error sending report to Arecibo")

        return "An error occured while processing your request."



def make_app(app, global_conf, **kw):
    return AreciboMiddleware(app, global_conf=global_conf, **kw)

