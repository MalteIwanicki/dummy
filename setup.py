# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='myApp',
    version='0.1.0',
    description='myApp',
    long_description=readme,
    author='Malte Iwanicki',
    author_email='malteiwa@gmail.com',
    url='https://github.com/malteIwanicki/dummy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

