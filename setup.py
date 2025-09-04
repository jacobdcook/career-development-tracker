#!/usr/bin/env python3
"""
Setup script for Cybersecurity Job Search Tracker
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cybersecurity-job-tracker",
    version="1.0.0",
    author="Jacob Cook",
    author_email="jacobdcook@example.com",
    description="A comprehensive desktop application for managing structured schedules and career development plans",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacobdcook/career-development-tracker",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Education",
        "Topic :: Office/Business",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "cybersecurity-tracker=enhanced_cybersecurity_tracker:main",
        ],
    },
    keywords="cybersecurity, job-search, certification, security+, planning, productivity",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/cybersecurity-job-tracker/issues",
        "Source": "https://github.com/yourusername/cybersecurity-job-tracker",
        "Documentation": "https://github.com/yourusername/cybersecurity-job-tracker#readme",
    },
)
