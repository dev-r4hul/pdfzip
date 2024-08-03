from setuptools import setup, find_packages

setup(
    name="pdfzip",
    version="0.1.0",
    author="Theeko74, ChatGPT",
    author_email="author@example.com",
    description="A simple PDF compressor using Ghostscript",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pdfzip",
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
