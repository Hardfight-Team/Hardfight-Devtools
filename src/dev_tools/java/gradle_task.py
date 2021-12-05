# External imports
import sys

# Internal imports
from dev_tools.utils.exec_cmd import exec_cmd


# Gradle wrappers scripts
GRADLE_WRAP = './gradlew'
GRADLE_WRAP_WINDOWS = './gradlew.bat'


def gradle_task(task: str):
    """Runs a gradle task"""
    gradlew = GRADLE_WRAP if sys.platform != 'win32' else GRADLE_WRAP_WINDOWS
    exec_cmd(f'{gradlew} {task}')


# Script version of the function
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <task>', file=sys.stderr)
        sys.exit(1)
    gradle_task(sys.argv[1])
