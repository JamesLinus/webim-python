#!/usr/bin/env python

from setuptools import setup
import errdb

setup(name="webim",
      version=webim.__version__,
      description="Python webim client",
      long_description=open("README.md").read(),
      author="Ery Lee",
      author_email="ery.lee@gmail.com",
      maintainer="Ery Lee",
      maintainer_email="ery.lee@gmail.com",
      url="http://github.com/webim/webim-python",
      download_url="http://nextalk.im",
      py_modules=["webim"],
      classifiers=[
        "Development Status :: 1 - Beta/Unstable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ])

