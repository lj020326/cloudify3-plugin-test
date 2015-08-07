__author__ = 'Lee'

from setuptools import setup

setup(
    zip_safe=True,
    name='cloudify-lee-plugin',
    version='1.0',
    author='Lee',
    author_email='lee.james.johnson@gmail.com',
    packages=[
        'lib'
    ],
    license='LICENSE',
    description='Playground plugins',
    install_requires=[
        'cloudify-plugins-common>=3.1'
    ]
)
