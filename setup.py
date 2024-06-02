from setuptools import setup, find_packages
setup(
    name='htmlFetcher',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    author='Md Anisur Rahman',
    author_email='anisurrahman06046@gmail.com',
    description='A simple package to fetch HTML data from a website',
    url='https://github.com/AnisurRahman06046/fetchHtml_website.git',  # Update with your actual GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)