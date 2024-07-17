#!/usr/bin/python3.10
"""
setup function to be run when creating packages
command to be typed in:
python setup.py sdist               # for tag.gz
python setup.py bdist_wheel         # for wheel installer
python setup.py sdist bdist_wheel   # for both
"""

from setuptools import setup

setup(
    name='sziller_assist',  # package name, used at pip or tar.
    version='0.0.1',  # version Nr.... whatever
    packages=["time_format", "cryptography", "DataVisualizer"],  # string list of packages to be translated
    url='',  # if url is used at all
    license='',  # ...
    author='sziller',  # well obvious
    author_email='szillerke@gmail.com',  # well obvious
    description='Sziller tools',  # well obvious
    install_requires=["pytest"],  # ATTENTION! Wheel file needed, depending on environment
    dependency_links=[],  # if dependent on external projects
)
