# encoding=utf-8
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='mentorship',
    version='1.0',
    author='Oksana Odynska',
    author_email="oksana.odynska.lv@gmail.com",
    description="long description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    url="https://github.com/oksanaJames/dqe_mentorship.git",
    packages=find_packages()
)
