=======
Loaders
=======

Loaders is a simple Django app to conduct Web-based loaders. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "loaders" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'loaders',
    ]

2. Include the loaders URLconf in your project urls.py like this::

    path('loaders/', include('loaders.urls')),

3. Run `python manage.py migrate` to create the loaders models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a loading (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/loaders/ to participate in the loading.

