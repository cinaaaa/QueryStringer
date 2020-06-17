import re
from setuptools import setup
from os import path

project_path = path.abspath(path.dirname(__file__))

with open(path.join(project_path, 'README.md')) as f:
    long_description = f.read()

setup(
    name = 'querystringer',
    packages = ['querystringer'],
    license = 'MIT',
    version = '0.0.2',
    description = 'Simple middleware for django to extract string queries from urls',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author = 'Sina Farhadi',
    author_email = 'sina.farhadi.cyber@gmail.com',
    url = 'https://github.com/E-RROR/QueryStringer/',
    keywords = ['django','strings','query','query stringer'],
    classifiers = [
        "Framework :: Django"
    ],
)
