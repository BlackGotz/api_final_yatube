"""
WSGI config for api_final_yatube project.

Этот файл содержит настройки для запуска проекта на WSGI-сервере.
WSGI (Web Server Gateway Interface) является стандартом для синхронных веб-приложений на Python
и широко используется для развертывания Django-приложений в продакшене.

Для получения дополнительной информации о WSGI и его использовании в Django, посетите:
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube_api.settings')

# Получаем WSGI-приложение для использования сервером
application = get_wsgi_application()
