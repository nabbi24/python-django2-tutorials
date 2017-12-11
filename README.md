# hosenka

## Setting up a Python development environment

We won't either commit `venv` files to git repos or add them to `.gitignore`.

All we have to do is to make 2 kinds of files:
- local `venv` files 
- a project `requirement.txt` which manage Python packages versions

### Procedure

#### Premises

- Python version is: 3.6

#### Common

1. Create a Python venv folder

    ```
    mkdir ~/.env
    cd ~/.env
    python3.6 -m vnev python-3.6
    cd python-3.6
    ```

1. Activate a Python venv

    ```
    source bin/activate
    ```

1. Ref: Deacticate

    When you want to deactivate, just run the below command:

    ```
    deactivate
    ```

#### Those who create an environment (Such as managers)

1. Create [YOUR_GIT_REPO]

    ```
    cd [YOUR_GIT_REPO_ROOT_DIR]
    ```
    
1. Install Python packages

    ```
    pip install django
    ```

1. Record packages versions in `requirement.txt`

    ```
    pip freeze > requirement.txt
    ```
    
1. Git commit

    ```
    git add .
    git commit -m "[YOUR_COMMENTS]"
    git push origin master # or [ANY_OF_YOUR_BRANCH]
    ```

### Those who prepare an environment (Such as developers)

1. Git clone

    ```
    git clone [YOUR_GIT_REPO]
    cd [YOUR_GIT_REPO_ROOT_DIR]
    ```

1. Install specified packages

    ```
    pip install -r requirement.txt
    ```
