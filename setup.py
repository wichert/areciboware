from setuptools import setup, find_packages

version = '1.0b1'

setup(name='areciboware',
      version=version,
      description="Arecibo error logging WSGI middleware",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
          ], 
      keywords='arecibo WSGI middleware',
      author='Wichert Akkerman',
      author_email='wichert@wiggy.net',
      url='http://pypi.python.org/pypi/areciboware',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "arecibo",
          "WebError",
      ],
      entry_points="""
      [paste.filter_app_factory]
      main = areciboware.middleware:make_app
      """,
      )
