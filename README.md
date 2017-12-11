# hosenka

## Setting up a Python development environment

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
