#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os
from setuptools import setup
from Cython.Distutils import build_ext
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np

# Version number
version = '0.4.6'

from pkg_resources import Requirement, resource_string
def read(fname):
    return resource_string(Requirement.parse("GPy"),fname)
    #return open(os.path.join(os.path.dirname(__file__), fname)).read()



setup(name = 'GPy',
      version = version,
      author = read('AUTHORS.txt'),
      author_email = "james.hensman@gmail.com",
      description = ("The Gaussian Process Toolbox"),
      license = "BSD 3-clause",
      keywords = "machine-learning gaussian-processes kernels",
      url = "http://sheffieldml.github.com/GPy/",
      packages = ["GPy.models", "GPy.inference.optimization", "GPy.inference", "GPy.inference.latent_function_inference", "GPy.likelihoods", "GPy.mappings", "GPy.examples", "GPy.core.parameterization", "GPy.core", "GPy.testing", "GPy", "GPy.util", "GPy.kern", "GPy.kern._src.psi_comp", "GPy.kern._src", "GPy.plotting.matplot_dep.latent_space_visualizations.controllers", "GPy.plotting.matplot_dep.latent_space_visualizations", "GPy.plotting.matplot_dep", "GPy.plotting"],
      package_dir={'GPy': 'GPy'},
      package_data = {'GPy': ['defaults.cfg', 'installation.cfg', 'util/data_resources.json', 'util/football_teams.json']},
      py_modules = ['GPy.__init__'],
      long_description=read('README.md'),
      install_requires=['numpy>=1.6', 'scipy>=0.9','matplotlib>=1.1', 'nose'],
      extras_require = {
        'docs':['Sphinx', 'ipython'],
      },
      classifiers=[
      "License :: OSI Approved :: BSD License"],
      #ext_modules = cythonize("GPy/kern/_src/*.pyx"),
      cmdclass = {'build_ext': build_ext},
      ext_modules = cythonize([Extension("cy_tree", ["GPy/kern/_src/cy_tree.pyx"],
                                         extra_compile_args=['-fopenmp','-std=c++0x'],
                                         extra_link_args=['-fopenmp','-std=c++0x'],
                                         language="c++",
                                         include_dirs=[np.get_include()]),
                               Extension("cy_sa_tree", ["GPy/kern/_src/cy_sa_tree.pyx"],
                                         extra_compile_args=['-fopenmp','-std=c++0x','-ftree-vectorize','-ftree-vectorizer-verbose=2'],
                                         extra_link_args=['-fopenmp','-std=c++0x'],
                                         language="c++",
                                         include_dirs=[np.get_include()]) ]),
      zip_safe = False
      )
