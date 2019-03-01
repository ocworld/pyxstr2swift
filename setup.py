# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', mode='r', encoding='utf-8') as f:
    license_text = f.read()

setup(
    name='nart',
    version='1.0',
    description='NART: Naver RealTime Keyword',
    long_description=readme,
    author='Keunhyun Oh',
    author_email='ocworld@gmail.com',
    url='https://github.com/ocworld/nart',
    license=license_text,
    packages=find_packages(exclude=('tests', 'docs')),
    platforms=['any'],
    install_requires=[
        'requests==2.21.0',
        'schedule==0.6.0',
        'beautifulsoup4==4.7.1',
        'python-crontab==2.3.6',
        'schedule==0.6.0',
    ],
    setup_requires=[
        'pytest-runner==4.4',
    ],
    tests_require=[
        'pytest==4.3.0',
    ],
    entry_points={
        'console_scripts': ['nart=nart.main:main'],
    },
    classifiers={
        'Programming Language :: Python',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: News/Diary',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    },
    project_url={
        'Bug Reports': 'https://github.com/ocworld/nart/issues',
        'Source': 'https://github.com/ocworld/nart'
    }
)
