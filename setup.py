# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyxstr2swift',
    version='0.1.0.dev1',
    description='Python package for a xcode strings file to a swift localized string file',
    long_description=readme,
    author='Keunhyun Oh',
    author_email='ocworld@gmail.com',
    url='https://github.com/ocworld/pyxstr2swift',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': ['xstr2swift=main.__main__:main'],
    },
    classifiers={
        'Environment :: Console',
        'Environment :: MacOS X',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators'
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    },
)