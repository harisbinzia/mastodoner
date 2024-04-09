try:
    from setuptools import setup, find_packages
except ImportError:
    # Handle the case where setuptools is not installed
    print("Setuptools is required to install this package.")
    print("Please install setuptools using 'pip install setuptools'.")
    exit(1)

import codecs

with codecs.open("mastodoner/version.py", "r", "utf-8") as f:
    exec(f.read())

with codecs.open("README.md", "r", "utf-8") as f:
    long_description = f.read()

setup(
    name="mastodoner",
    version=version,
    author="Haris Bin Zia",
    author_email="harisbinzia@hotmail.com",
    description="A package for crawling Mastodon instances",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harisbinzia/mastodoner",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mastodoner = mastodoner.cli:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests',
    ],
)
