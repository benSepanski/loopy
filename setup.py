#!/usr/bin/env python
# -*- coding: latin1 -*-

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py

setup(name="loopy",
      version="2011.1",
      description="An automatic loop generator for OpenCL",
      long_description="",
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        ],

      install_requires=[
          "pyopencl>=2011.1", "pymbolic", "cgen", "islpy"
          ],

      author="Andreas Kloeckner",
      url="http://pypi.python.org/pypi/pytools",
      author_email="inform@tiker.net",
      license = "MIT",
      packages=["loopy"],

      # 2to3 invocation
      cmdclass={'build_py': build_py})
