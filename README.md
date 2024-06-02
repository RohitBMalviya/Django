<INSTALLATION>
Create .venv
pip -m venv filename(.venv)

<MODULES>
pip install Django
pip install django-tailwind
pip install 'django-tailwind[reload]'
python manage.py tailwind install

<DJANGO SETUP>
TO create Project
python manage.py startproject projectname
To create ProjectApp
python manage.py startapp appname

<TAILWIND>
python manage.py tailwind init
Add in setting.py of Project
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'

<TO INJECT HTML(template)>
Add in setting.py
TEMPLATES = [
{
'DIRS': ['templates']
}
]

<TO INJECT CSS>
Add in setting.py of Project
import os
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
Add in Html
{% load static %}
<link rel="stylesheet" href="{% static 'style.css' %}" />
