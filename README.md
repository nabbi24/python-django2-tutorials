# hosenka

Welcome.

---

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

1. (ref) Deacticate

    When you want to deactivate it, just run the below command:

    ```
    deactivate
    ```

#### Those who create an environment (such as managers)

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

### Those who prepare an environment (such as developers)

1. Git clone

    ```
    git clone [YOUR_GIT_REPO]
    cd [YOUR_GIT_REPO_ROOT_DIR]
    ```

1. Install specified packages

    ```
    pip install -r requirement.txt
    ```

---

## Create a Django project

###### (ref) Public tutorials

https://docs.djangoproject.com/ja/2.0/intro

1. Start a project

    ```
    cd [YOUR_GIT_REPO_ROOT_DIR]
    django-admin startproject mysite .
    ```
    
    ###### Dirs
    
    ```
    .
    ├── mysite
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
    ```

1. Modify `hosenka/settings.py`

    - Language
    - Timezone

1. Migrate (Setting up DB)

    ```
    python manage.py migrate
    ```

1. Create a super user

    ```
    python manage.py createsuperuser
    ```

1. Run the server

    ```
    python manage.py runserver
    ```
    
    Now you can access:
    
    - `http://127.0.0.1:8000`
    - `http://127.0.0.1:8000/admin`
    
    ###### Dirs
    
    ```
    .
    ├── db.sqlite3
    ├── mysite
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
    ```

---

## Create apps

### Create loaders

1. Create an app

    ```
    python manage.py startapp loaders
    ```
    
    ###### Dirs

    ```
    .
    ├── loaders
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── mysite
    └── manage.py
    ```

1. Define models

    1. Modify `loaders/models.py`

    1. Make migrations

        ```
        python manage.py makemigrations loaders
        ```
    
    1. (ref) Check what is planned
    
        ```
        python manage.py sqlmigrate loaders 0001
        ```

        or

        ```
        python manage.py check
        ```
    
    1. Execute migrations
    
        ```
        python manage.py migrate
        ```
