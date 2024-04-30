# python3.11 setup.py bdist_wheel

from setuptools import setup, find_packages

setup(
    name="itsdangerous",
    version="2.2.0",
    description="FIPS compliant version of itsdangerous.",
    packages=find_packages(),
)
