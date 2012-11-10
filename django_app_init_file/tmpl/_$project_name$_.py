# -*- coding: utf-8 -*-
"""
Web app initial data.
Usage from main project directory::

    $> python -m app.init

Assuming project structure is something like::

   <projectname>/
       manage.py
       app/
           init.py
           <project-app-1>/
           <project-app-2>/
           ...
       ...

...and project manage.py contains setup function.
"""

def load_users():
    from django.contrib.auth.models import User

    admin, created = User.objects.get_or_create(
        username = "admin",
        email = "admin@admin.com",
        is_superuser = True,
    )
    admin.is_staff = True
    admin.set_password("admin")
    admin.save()

    return dict(
        admin = admin,
    )


def load():
    load_users()


if __name__ == '__main__':
    import manage
    manage.setup()
    load()
