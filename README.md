# Silk Road

We aim to make it easier to calculate the fees of employees which makes them happier.

---

## Setting up a Python development environment

We won't either commit `venv` files to git repos or add them to `.gitignore`.

All we have to do is to make 2 kinds of files:
- local `venv` files in `~/.env`
- a project `requirement.txt` which manage Python packages versions

### Procedure

#### Precondition

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

###### Caution:
This process is for the first time only.    
If you are a following developer, move to the next section.

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

1. Modify `silk-road/settings.py`

    - Language
    - Timezone

1. Migrate (Setting up DB)

    ```
    python manage.py migrate
    ```

1. Run the server

    ```
    python manage.py runserver
    ```
    
    Now you can access:
    
    - `http://127.0.0.1:8000`
    
    You can stop the server to click `Ctrl + C`.
    
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

---

## Create a super user

1. Create a super user

    ```
    python manage.py createsuperuser
    ```

    Now you can access after run the server:
    
    - `http://127.0.0.1:8000/admin`
  
## Add an app config

1. Modify 'mysite/settings.py'

    Add a loaders' config to `INSTALLED_APPS`:

    ```
    INSTALLED_APPS = [
        'loaders.apps.LoadersConfig',
        ...
    ]
    ```

1. Modify `loaders/models.py` and `loaders/views.py`

## Use templates

1. Create directories

    ```
    mkdir -p loaders/templates/loaders
    ```

1. Make htmls such as `index.html` in `loaders/templates/loaders`

1. Modify `loaders/views.py`

1. Use Django shortcuts in `views.py`

1. In templates, Replace hard-coded urls to `url` functions.

## Add namespaces

1. Add `APP_NAME` to `loaders/urls.py`

1. Use the name in templates

1. In `url` functions in templates, Add namespaces to url-names.

## Finally

- Dir

    ```
    silk-road
    ├── db.sqlite3
    ├── loaders
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   └── (...).pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── (...).py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   ├── models.py
    │   ├── static
    │   │   └── loaders
    │   │       ├── images
    │   │       │   └── background.gif
    │   │       └── style.css
    │   ├── templates
    │   │   └── loaders
    │   │       ├── detail.html
    │   │       ├── index.html
    │   │       └── results.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── mysite
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   └── (...).pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── requirement.txt
    └── templates
        └── admin
            ├── base_site.html
            └── index.html
    ```
