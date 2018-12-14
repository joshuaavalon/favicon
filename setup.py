from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="joshuaavalon-favicon",
    version="1.0.0",
    author="Joshua Avalon",
    url="https://github.com/joshuaavalon/favicon",
    description="Download favicon from urls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    packages=["joshuaavalon.favicon"],
    install_requires=[
        "Pillow>=5.3.0",
        "beautifulsoup4>=4.6.3",
        "requests>=2.21.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
)
