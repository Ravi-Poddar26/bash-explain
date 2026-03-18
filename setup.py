#!/usr/bin/env python3
"""
Setup script for BashExplain
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bashexplain",
    version="1.0.0",
    author="Ashish Singh, Ravi Poddar",
    author_email="ravipoddar2006@gmail.com,ashishsingh.mail26@gmail.com",
    description="A command-line tool to explain Bash commands, errors, and scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/singhashish12238-pixel/bash-explain",
    project_urls={
        "Bug Tracker": "https://github.com/singhashish12238-pixel/bash-explain/issues",
        "Documentation": "https://github.com/singhashish12238-pixel/bash-explain#readme",
        "Source Code": "https://github.com/singhashish12238-pixel/bash-explain",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: System Administrators",
        "Topic :: Education",
        "Topic :: System :: Shells",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
    ],
    keywords="bash shell terminal cli education learning command-line",
    py_modules=["bash_explain"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "bashexplain=bash_explain:main",
        ],
    },
    install_requires=[
        # No external dependencies - pure Python!
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.900",
        ],
    },
)
