# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="traductor-guarani",
    version="0.1.0",
    author="jota",
    description="Traductor de español a guaraní con API web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "flask>=3.1.2",
        "requests>=2.32.5",
    ],
    python_requires=">=3.8",
)