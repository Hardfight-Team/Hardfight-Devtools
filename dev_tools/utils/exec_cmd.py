# External imports
import subprocess
import shlex
import sys
import os


def exec_cmd(cmd: str, cwd: str = '.'):
    """Executes a shell command
    Exits the script is the return code is not 0

    :param cmd: Command to execute
    :type cmd:    str
    :param cwd: Working directory, defaults to '.'
    :type cwd:    str, optional
    """
    try:
        splitted_cmd = shlex.split(cmd)
        process = subprocess.run(splitted_cmd, cwd=cwd)
        if process.returncode != 0:
            sys.exit(process.returncode)
    except KeyboardInterrupt:
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)


# Script version of the function
if __name__ == '__main__':
    len_argv = len(sys.argv)
    if len_argv == 1 or len_argv > 3:
        print(f'Usage: {sys.argv[0]} <cmd> [cwd]', file=sys.stderr)
        sys.exit(1)
    if len_argv == 3:
        exec_cmd(sys.argv[1], sys.argv[2])
    else:
        exec_cmd(sys.argv[1])
