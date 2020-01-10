from setuptools import setup, find_packages
from pathlib import Path

with Path('README.md').open() as readme:
    readme = readme.read()

version = "1.0.1"

setup(
    name='remu-operator',
    version=version if isinstance(version, str) else str(version),
    keywords="compiler, operator precedence, operator associativity, resolver",
    description=
    "A framework to separate resolution of operator precedence and associativity from parsing time",
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3',
    url='https://github.com/RemuLang/remu-operator',
    author='thautawarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    entry_points={"console_scripts": []},
    install_requires=[],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
