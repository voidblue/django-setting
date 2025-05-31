"""
WSGI config for djangosetting project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# 동기 프레임워크에 관련된 설정

import os
import django

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosetting.api.settings')



application = get_wsgi_application()


call_command("makemigrations", interactive=False)
call_command("migrate", interactive=False)