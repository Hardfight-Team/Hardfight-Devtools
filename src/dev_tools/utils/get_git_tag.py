# External imports
import subprocess


# Command to get the current recent tag
GIT_SHORT_REV_CMD = ['git', 'describe', '--abbrev=0', '--tags']


def get_git_tag() -> str:
    """Returns the most recent tag in the git branch

    :return:    Recent git tag
    :rtype:     str
    """
    short_rev = subprocess.check_output(GIT_SHORT_REV_CMD).decode('ascii')
    short_rev = short_rev.strip()
    return (short_rev)


# Script version of the function
if __name__ == '__main__':
    short_rev = get_git_tag()
    print(short_rev)
