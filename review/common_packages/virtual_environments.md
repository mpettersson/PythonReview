
Virtual Environments
====================

SEE: https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyenv-pyenv-virtualenv-virtualenvwrappe


venv
----
- SEE: https://docs.python.org/3/library/venv.html
- A part of standard library/official.



virtualenv
----------
- Basic virtual environment tool; copies python files to a specified directory, then modifies path to use them.
- NOT a part of standard library (have to install it), but blessed by PyPA (Python Packaging Authority).
- Allows for different python versions (see caveats below).
- After activated, will install packages to env dir.

### Basic Commands
- Install virtualenv package:

        pip3 install virtualenv
    
- Create a virtualenv:

        virtualenv env_name                         # env_name at curr dir (with default python)
        virtualenv /path/to/env_name                # at specified location (with default python)        
        virtualenv -p python3 /path/to/env_name     # with specified version (must be on system) & dir.
       
- Activate/Deactivate virtualenv:

        /path/to/env_name/bin/activate              # Activate virtual environment.
        deactivate                                  # Deactivate virtual environment.

- NOTE: Virtualenv's -p option will allow any python version INSTALLED to be used, and must either be the path to the
interpreter, OR, a command that is tied to a python interpreter (in path).


virtualenvwrapper
-----------------
- SEE: https://virtualenvwrapper.readthedocs.io/en/latest/index.html
- Extensions to virtualenv.
- NOT a part of standard library (have to install it).
- Allows for different python versions (see caveats below).
- ALL virtual environments are in a central location (in $PROJECT_HOME, or $HOME/.virtualenvs by default.).

### Basic Commands
- Install virtualenv package:

        pip3 install virtualenv
    



