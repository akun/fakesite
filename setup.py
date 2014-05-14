#!/usr/bin/env python


from setuptools import setup, find_packages
from pip.req import parse_requirements

def get_reqs():
    install_reqs = parse_requirements('requirements.txt')
    return [str(ir.req) for ir in install_reqs]

from fakesite import VERSION


setup(
    name='fakesite',
    version=VERSION,
    description='A fake site for spider testing',
    author='akun',
    author_email='6awkun@gmail.com',
    license='MIT License',
    url='https://github.com/akun/fakesite',
    package_dir={'': 'fakesite'},
    packages=find_packages('fakesite'),
    install_requires=get_reqs(),
    test_suite='nose.collector',
)
