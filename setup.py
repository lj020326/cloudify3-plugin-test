__author__ = 'Lee'

from setuptools import setup

setup(
    zip_safe=True,
    name='test-echo-plugin',
    version='1.0',
    author='Lee',
    author_email='lee.james.johnson@gmail.com',
    packages=[
        'plugin'
    ],
    license='LICENSE',
    description='Test Echo plugin',
    install_requires=[
#        "cloudify-plugins-common>=3.3a3"
        "cloudify-plugins-common>=3.2"
    ],
    test_requires=[
#        "cloudify-dsl-parser>=3.3a3"
        "cloudify-dsl-parser>=3.2",
        "nose"
    ]
)
