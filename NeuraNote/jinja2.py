from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'get_static_prefix': staticfiles_storage.url,
        'url': reverse,
    })
    return env
