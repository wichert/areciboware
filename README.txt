``areciboware`` is a small WSGI middleware component that will report
unhandled exceptions to an `Arecibo`_ instance. This provides a convenient
system to collect and analyse errors in an application. 

Usage
=====

To use ``areciboware`` you need to have a running Arecibo instance. You will
needs its URL and its public key to setup the middleware.

paste.deploy
-------------
If you are using `Paste Deployment`_ to start your website you can define
an arecibo *filter* in your ``.ini`` file::

   [filter:arecibo]
   use = egg:areciboware#main
   url = http://my-arecibo.appspot.com/v/1/
   account = your-arecibo-public-key

   [app:yourapp]
   ..

   [pipeline:main]
   pipeline =
       arecibo
       yourapp


Manual
------
You can also manually add the middleware to your WSGI pipeline in your python
code. Here is a simple example::

     from areciboware.middleware import AreciboMiddleware

     app = AreciboMiddleware(app, url="http://my-arecibo.appsot.com/v/1/",
          account="your-arecibo-public-key")
     return app


.. _Arecibo: http://areciboapp.com/
.. _Paste Deployment: http://pythonpaste.org/deploy/
