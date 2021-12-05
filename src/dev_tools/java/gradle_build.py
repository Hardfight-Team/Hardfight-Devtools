# External imports
import sys

# Internal imports
from dev_tools.utils.exec_cmd import exec_cmd


# Gradle wrappers scripts
GRADLE_WRAP = './gradlew'
GRADLE_WRAP_WINDOWS = './gradlew.bat'


def gradle_build():
    """Builds the client using gradle"""
    gradlew = GRADLE_WRAP if sys.platform != 'win32' else GRADLE_WRAP_WINDOWS
    exec_cmd(f'{gradlew} build')


# Script version of the function
if __name__ == '__main__':
    gradle_build()
