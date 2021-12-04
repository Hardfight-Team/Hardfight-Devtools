# External imports
from typing import Callable, Dict, Optional, cast
import collections
import time
import sys


# Task type and registry
Task = collections.namedtuple('Task', 'name desc run')
TASK_REGISTRY: Dict[str, Task] = {}

# Help message
HELP_MESSAGE = """
HARDFIGHT DEVTOOLS

        Devtools is a Python utils tools to make building, testing
        and deploying hardfight projects easy. It offers all the scripting
        power of the python language with a lightweight API to register
        simple tasks in one script.

USAGE
        %s <task_1> [task_2] ...

TASKS
"""


def dev_tools_task(name: str, desc: Optional[str] = None) -> Callable:
    """Devtools task decorator
    It registers a task and makes it executable from the dev_tools script

    :param name:    Task name
    :type name:     str
    :param desc:    Task description (displayed in --help), defaults to None
    :type desc:     Optional[str], optional

    :return:            Register routine
    :rtype:             Callable
    """
    def register_task(func: Callable):
        def execute_task():
            print(f"Starting '{name}' task")
            start = time.time()
            func()
            end = time.time()
            print(f"Task '{name}' finished (in {int(end - start)}s)")
        TASK_REGISTRY[name] = Task(name, desc, execute_task)
    return (register_task)


def dev_tools_main():
    """Devtools script entry point
    It performs the tasks given in the command line
    """
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <task_1> ...', file=sys.stderr)
        sys.exit(1)

    # Help option
    if '-h' in sys.argv or '--help' in sys.argv:
        global HELP_MESSAGE
        for task_obj in TASK_REGISTRY.values():
            desc_str: str
            if task_obj.desc is None:
                desc_str = 'No description provided'
            else:
                desc_str = cast(str, task_obj.desc)
            HELP_MESSAGE += f'        {task_obj.name}\t{desc_str}\n'
        print(HELP_MESSAGE % sys.argv[0])
        sys.exit(0)

    # Run tasks
    tasks_list = sys.argv[1:]
    for task in tasks_list:
        task_obj = TASK_REGISTRY.get(task, None)
        if task_obj is None:
            print(f"Skipping unknown '{task}' task", file=sys.stderr)
            continue
        task_run = cast(Task, task_obj).run
        task_run()
