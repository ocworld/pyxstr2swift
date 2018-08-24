# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()  # type: str

with open('LICENSE') as f:
    license = f.read() # type: str

setup(
    name='pyxstr2swift',
    version='0.1.0.dev16',
    description='Python package for a xcode strings file to a swift localized string file',
    long_description=readme,
    author='Keunhyun Oh',
    author_email='ocworld@gmail.com',
    url='https://github.com/ocworld/pyxstr2swift',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    platforms=['any'],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': ['xstr2swift=pyxstr2swift.pyxstr2swift:main'],
    },
    classifiers={
        'Environment :: Console',
        'Environment :: MacOS X',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/ocworld/pyxstr2swift/issues',
        'Source': 'https://github.com/ocworld/pyxstr2swift'
    }
)
