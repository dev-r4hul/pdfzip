from setuptools import setup, find_packages

setup(
    name="pdfzip",
    version="0.1.0",
    author="Rahul Choudhary",
    author_email="goodluckrahul@yahoo.com",
    description="A simple PDF compressor using Ghostscript",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dev-r4hul/pdfzip",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add dependencies here if needed
    ],
    entry_points={
        "console_scripts": [
            "pdfzip=pdfzip.compressor:main",
        ],
    },
)
