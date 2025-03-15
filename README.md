# Проект API для Yatube

API для работы с постами сервиса Yatube, предоставляет доступ для чтения публикаций и комментариев всем пользователям, авторизованным пользователям позволяет публиковать новые посты и комментарии.

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```shell
git clone git@github.com:BlackGotz/api_final_yatube.git
```

```shell
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```shell
python3 -m venv .venv
```

```shell
source .venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```shell
python -m pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

Выполнить миграции:

```shell
python manage.py migrate
```

Запустить проект:

```shell
python manage.py runserver
```

## Примеры некоторых запросов

P.S. примеры всех запросов можно посмотреть в документации по адресу /redoc/

- Публикация поста

```postman
POST /api/v1/posts/
{
    "text": "string"
}
```

- Получение постов постранично

```postman
GET /api/v1/posts/?limit=10&offset=10
```

- Получение всех комменатриев

```postman
GET /api/v1/posts/{post_id}/comments/
```

- Удаление комментария

```postman
DEL /api/v1/posts/{post_id}/comments/{comment_id}/
```
