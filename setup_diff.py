--- setup.py


+++ setup.py
from setuptools import setup, find_packages

setup(
    name="blackcoffer-article-scraper",
    version="1.0.0",
    description="A web scraper for extracting articles from BlackCoffer Insights",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4>=4.9.3",
        "requests>=2.25.1",
        "pandas>=1.3.3",
        "lxml>=4.6.3",
    ],
    python_requires=">=3.6",
)
