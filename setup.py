#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
    'requests==2.5.1',
]

test_requirements = [
    'pytest==2.6.4',
]

setup(
    name='meteora',
    version='0.1.0dev0',
    description='A performance testing web application',
    long_description='A performance testing web application',
    author='raulcd',
    author_email='raulcumplido@gmail.com',
    url='https://github.com/raulcd/meteora',
    packages=[
        'meteora',
    ],
    package_dir={'meteora':
                 'meteora'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='meteora',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
