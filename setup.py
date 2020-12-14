import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='utils',
    version='0.0.1',
    author='Dorjee Gyaltsen',
    packages=find_packages(exclude=['tests']),
    package_data={
        'utils': ['utils/common.py', 'utils/bio.py', 'tm.py', 'restriction_enzymes.txt']
    },
    description='Python package for some of the common (mundane) tasks and also some specific bioinformatics parsing.',
    long_description=README,
    keywords='',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.7',
    ]
)
