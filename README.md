# Bookstore System



## Getting started

clone repository.

install python 3.12.o (skip step if already installed)

run command "pip install pipenv"

## creating virtual environment

to create virtual environment with projects dependwencie packages ,in this projects repo run cmd command "pipenv install"

## running project

in this projects repo run cmd command "pipenv shell" to activate virtual env with its requirements.



## deployment settings


ensure that deploying server has environment varriable set to>  DJANGO_ALLOWED_HOSTS


if deploying locally you can edit this line in settings.py


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"# for production mode


also ensure you have configured DATABASES field in settings.py connect your database











