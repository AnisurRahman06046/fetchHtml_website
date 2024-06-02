from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "readme.MD").read_text()
# Setting up
setup(
name='htmlExtractor',  
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    author='Md Anisur Rahman',
    author_email='anisurrahman06046@gmail.com',
    description='A simple package to fetch HTML data from a website',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/AnisurRahman06046/fetchHtml_website.git',  # Your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)