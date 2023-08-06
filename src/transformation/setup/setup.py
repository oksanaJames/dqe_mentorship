from setuptools import setup

setup(
    name='sherlock',
    version='1.0',
    author='Kylie James',
    packages=['sherlock'],
    description='Description',
    package_data={'': ['*.txt']},
    entrypoints={'console_scripts': ['sherlock = sherlock.sherly_dog:main']},
)
