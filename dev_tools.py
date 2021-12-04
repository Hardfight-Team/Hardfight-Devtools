#! /usr/bin/env python3

#
# Hardfight Devtools 2021
# dev_tools.py
# Hardfight Devtools script for the Devtools project
#


# External imports
import sys

# Internal imports
from dev_tools.utils.exec_cmd import exec_cmd
from dev_tools.utils.find_paths import find_paths
from dev_tools.utils.silent_remove import silent_remove
from dev_tools.dev_tools_api import dev_tools_main, dev_tools_task


@dev_tools_task(name='dist',
                desc='Build the python package (in the dist directory)')
def build_dist():
    exec_cmd(f'{sys.executable} -m build')


@dev_tools_task(name='pep8',
                desc='Checks if python code respects PEP8')
def pep8():
    exec_cmd(f'{sys.executable} -m pycodestyle')


@dev_tools_task(name='mypy',
                desc='Type checks python code')
def mypy():
    exec_cmd(f'mypy .')


@dev_tools_task(name='clean',
                desc='Clean the repository from temporary files')
def clean():
    files_to_remove = ['dist']
    recursive_targets = [
        '__pycache__', '*.pyc', '.mypy_cache',
        '.DS_Store', '*.egg-info'
    ]
    for target in recursive_targets:
        files_to_remove.extend(find_paths('.', target))
    for file in files_to_remove:
        print(f"Removed '{file}'")
        silent_remove(file)


# Script entry point
if __name__ == '__main__':
    dev_tools_main()
