# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in funding_management/__init__.py
from funding_management import __version__ as version

setup(
	name='funding_management',
	version=version,
	description='App for manage funding',
	author='Akram Mutaher',
	author_email='a.mutaher@partner-cons.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
