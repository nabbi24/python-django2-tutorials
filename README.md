# hosenka

## Setting up a Python development environment

We won't either commit `venv` files to git repos or add them to `.gitignore`.

All we have to do is to make 2 kinds of files:
- local `venv` files 
- a project `requirement.txt`.

### Procedure

1. Create a Python venv folder

    ```
    mkdir ~/.env
    cd ~/.env
    python -m vnev python-3.6.3
    cd python-3.6.3
    ```

1. Install Python packages

    ```
    source bin/activate
    pip install django
    ```

1. Preserve package versions

    ```
    cd [YOUR_PROJECT_ROOT_DIR]
    pip freeze > requirement.txt
    ```
