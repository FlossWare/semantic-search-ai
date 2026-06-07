"""
Semantic Search AI - Advanced semantic search toolkit

Production-grade search enhancements: hybrid search, reranking, filtering.
"""

from setuptools import setup, find_packages

setup(
    name="semantic-search-ai",
    version="0.2",
    author="FlossWare (sfloess)",
    description="Advanced semantic search toolkit for AI applications",
    long_description=open("../README.md").read() if __file__ else "",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/cee/sfloess/semantic-search-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "sentence-transformers>=2.2.0",
        "numpy>=1.21.0",
    ],
)
