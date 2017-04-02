import os
from setuptools import setup

setup(
    name="mookfist-lled-controller",
    version="0.0.1",
    author="mookfist",
    author_email="mookfist@gmail.com",
    url="https://github.com/mookfist/mookfist-lled-controller",
    scripts=['lled.py'],
    install_requires=[
        'docopt',
        'colorama'
    ]
)
