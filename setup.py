from setuptools import setup, find_packages


setup(
    name="code_to_text",
    version="0.1.0",
    author="Benjamin QUINET",
    author_email="benjamin.quinet59b@gmail.com",
    description="A Python package to concatenate code files into a single text file.",
    long_description=open('readme.md').read(),
    url="https://github.com/Benalieur/CODE_TO_TEXT.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)