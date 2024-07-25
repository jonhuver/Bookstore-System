"""
Django settings for Bookstore project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.


BASE_DIR = Path(__file__).resolve().parent.parent  #prev b4 deploy




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$t&1o$74x&=8e1cv($!_mzq=391-+gscveo41zgajy_rl3vfkv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =False #True

#ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['.vercel.app','now.sh','127.0.0.1','localhost',"pg-2e49feb8-jonahmungainyokabi-5b3f.f.aivencloud.com"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'slick_reporting',
    'crispy_forms',
    'crispy_bootstrap4' ,
    

    'Users',#1
    'books',
    
    'rest_framework',   # for json web tokens
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Bookstore.urls'

#templates_directory="C:/projects/pythonprojects/Bookstore System/Bookstore/"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':['templates','static'] ,#[(templates_directory + 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Bookstore.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



#DATABASES = {
    #'default': {
		#'ENGINE': 'django.db.backends.mysql',
		#'NAME': 'bokstore',
		#'USER': 'root',
		#'PASSWORD': 'J.m@20221578',
		#'HOST':'localhost',
		#'PORT':'3306',
	#}

   
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_9362e2dd_1714_4a50_8de9_a3268570815b',
        'USER': 'u_9362e2dd_1714_4a50_8de9_a3268570815b',
        'PASSWORD': 'N09LF1fd43aXhsLuL0U48Mu11wx5WOw8LA2Mb6N4f7u2r94atcb2',
        'HOST': 'pg.rapidapp.io',
        'PORT': '5433',
    }
}


EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
       
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        
    ),
}


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ =False #True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/




STATIC_URL = 'static/'



MEDIA_ROOT="/media/"  #path for media files
MEDIA_URL = '/media/' 

MEDIA_ROOT=os.path.join(BASE_DIR,'media')


STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),

                  
                  )
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')


STATIC_ROOT = os.path.join(BASE_DIR,  'static_media/') #prev deploy b4

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
