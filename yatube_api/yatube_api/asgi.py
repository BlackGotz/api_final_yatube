"""
ASGI config for api_final_yatube project.

Этот файл содержит настройки для запуска проекта на ASGI-сервере.
ASGI (Asynchronous Server Gateway Interface) обеспечивает поддержку асинхронных веб-приложений,
что позволяет обрабатывать запросы более эффективно и поддерживать такие протоколы, как WebSocket.

Для получения дополнительной информации об ASGI и его использовании в Django, посетите:
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application


# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube_api.settings')

# Получаем ASGI-приложение для использования сервером
application = get_asgi_application()
