from setuptools import setup, find_packages
from distutils.core import Extension

VERSION = '0.1.1'


def requirements():
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()


def readme():
    with open('readme.md', 'r') as f:
        return f.read()


geolib = Extension('geolib', ['pygclib/geography/geodesic.c', 'pygclib/geography/geolib.c'])

setup(name='pygclib',
      version=VERSION,
      description='A library for paragliding races',
      long_description=readme(),
      url='https://github.com/igclib/pygclib',
      author='Téo Bouvard',
      author_email='teobouvard@gmail.com',
      license='GPL-3',
      packages=find_packages(include=['pygclib']),
      ext_modules=[geolib],
      install_requires=requirements(),
      scripts=['pygclib/bin/pygclib'],
      python_requires='>=3.5',
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      zip_safe=True)
