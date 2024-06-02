# INSTALLATION

## **Create .venv**

```
pip -m venv .venv
```

# MODULES

```
pip install Django
```

```
pip install django-tailwind
```

```
pip install 'django-tailwind[reload]' --> to reload the Django
```

```
python manage.py tailwind install --> to install tailwind in main project
```

```
pip install Pillow
```

# DJANGO SETUP

## To create Project

```
python manage.py startproject projectname
```

## To create ProjectApp

```
python manage.py startapp appname
```

## To runserver

```
python .\manage.py runserver
```

## Migration

```
python .\manage.py migrate
```

## To create super user

```
python .\manage.py createsuperuser
```

# TAILWIND SETUP

```
python manage.py tailwind init
```

## Add in setting.py of Project

```
TAILWIND_APP_NAME = 'theme'
```

```
INTERNAL_IPS = ['127.0.0.1']
```

```
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

## Add in basic.html of template folder

```
{% load static tailwind_tags %}
```

```
{% tailwind_css %}
```

**To activate the tailwind**

```
python manage.py tailwind start
```

# TO INJECT HTML(template)

## Add in setting.py

```
TEMPLATES = [
{
'DIRS': ['templates']
}
]
```

# TO INJECT CSS

## Add in setting.py of Project

```
import os
```

```
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
```

## Add in basic.html file or any html file

```
{% load static %}
```

```
<link rel="stylesheet" href="{% static 'style.css' %}" />
```

# Reload Django

## Add in setting.py

```
INSTALLED_APPS = [
   'django_browser_reload',
   ]
```

```
MIDDLEWARE = [
  "django_browser_reload.middleware.BrowserReloadMiddleware"
  ]
```

## Add in urls.py of project at last

```
path('**reload**',include('django_browser_reload.urls'))
```

# Media files such image to handle

## Add in setting.py

```
MEDIA_URL = 'media/'
MEDIA_ROOT = [os.path.join(BASE_DIR,'media')]
```

## Add in urls.py of project

```
from django.conf import settings
from django.conf.urls.static import static
```

```
urlpatterns = [
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

# Models

## To make sql table fields

```
python .\manage.py makemigrations
```

## To migrate

```
python .\manage.py migrate
```
