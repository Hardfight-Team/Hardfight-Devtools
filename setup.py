#! /usr/bin/env python3

#
# Hardfight Devtools 2021
# setup.py
# Hardfight Devtools setup.py template script
#


# External imports
import setuptools  # type: ignore
import pathlib


# Get the long description from the README file
PARENT_DIR = pathlib.Path(__file__).parent.resolve()
LONG_DESC = (PARENT_DIR / 'README.md').read_text(encoding='utf-8')


# Python package setup
setuptools.setup(
    name='hardfight_devtools',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    version='0.4',
    license='MIT',
    description='Devtools is a Python utils tools to make building, '
                'testing and deploying hardfight projects easy',
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    author='Eliot Maurice',
    author_email='procyx.io@gmail.com',
    url='https://github.com/Hardfight-Team/Hardfight-Devtools',
    keywords=['hardfight', 'build', 'test', 'script'],
    install_requires=['checksumdir', 'boto3'],
    python_requires='>=3.7, <4',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
)
