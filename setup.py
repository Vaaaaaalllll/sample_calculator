# WARNING: template code, may need edits
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sample_calculator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python calculator application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sample_calculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
        ],
    },
)
