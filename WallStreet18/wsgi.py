"""
WSGI config for WallStreet18 project.
application
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WallStreet18.settings")

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
