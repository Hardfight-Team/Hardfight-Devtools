<div>
     <p align="center">
        <img width="220" height="220" src="misc/files/readme/devtools_symbol.png" />
     </p>
     <h3 align="center">Hardfight Devtools</h3>
     <p align="center">Build, test and deploy Hardfight projects easly</p>
     <p align="center">
            <img src="https://github.com/Hardfight-Team/Hardfight-Devtools/actions/workflows/publish.yml/badge.svg" alt="publish"/>
     </p>
</div>    

## 💡 What is it

Devtools is a Python tool to make **building**, **testing** and **deploying** internal hardfight projects easy.  
It offers all the **scripting power** of the python language with a lightweight API to register **simple tasks** in one script.

## 🛠️ How to install

Hardfight devtools is available as a PyPi package, you can install it using:  
```pip install hardfight_devtools```  
Note that dev_tools is **assumed installed** to build any Hardfight project.

## ❓ How to use

This repository itself uses dev_tools to perform build and deploy routines.  

On a new project, create a `dev_tools.py` file on the root.  
To declare a new task, add the `@dev_tools_task` decorator to the function of your task.  

```python
from dev_tools.dev_tools_api import dev_tools_main, dev_tools_task 

@dev_tools_task(name='hello-world',
                desc='Prints "Hello world!" as an example task')
def print_hw():
    print('Hello world!')
```

Devtools provides a bunch of usefull scripts and functions for build, test and deploy automations (see `dev_tools.utils` module).  
Don't forget to call the `dev_tools_main` method at the end of your script to make it functional.  

```python
# Script entry point
if __name__ == '__main__':
    dev_tools_main()
```

You can then execute your tasks using: `python3 dev_tools.py <tasks_1> [task_2] ...`

### General conventions on hardfight projects

- If you need additional python scripts for your tasks, add them in the `misc/scripts` directory in your repository
- All files related to the meta-project or build (README images, requierments...) have to be in the `misc/files` directory in your repository
