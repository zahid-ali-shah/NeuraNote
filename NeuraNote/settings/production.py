from .base import *

DEBUG = False
DATABASES = {'default': env.db()}  # TODO Expects postgres://... from env
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
