from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя.
from django.db import models  # Импортируем базовые классы и функции для работы с моделями Django.

User = get_user_model()  # Получаем модель пользователя, которая может быть изменена (например, для кастомных пользователей).

# Модель для группы
class Group(models.Model):
    title = models.CharField(max_length=200)  # Заголовок группы, ограничение на 200 символов
    slug = models.SlugField(max_length=50, unique=True)  # Слаг для группы (уникальное значение, которое будет использоваться в URL)
    description = models.TextField()  # Описание группы (большой текст)

    def __str__(self):
        return self.title  # Возвращаем название группы в виде строки

# Модель для поста
class Post(models.Model):
    text = models.TextField()  # Основной текст поста
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)  # Дата и время публикации поста (автоматически заполняется при создании)
    author = models.ForeignKey(  # Внешний ключ на модель User (автор поста)
        User, on_delete=models.CASCADE, related_name='posts')  # Если пользователь удаляется, удаляются все его посты
    image = models.ImageField(  # Поле для загрузки изображения, связанное с постом (необязательное)
        upload_to='posts/', null=True, blank=True)  # Задаем путь для загрузки изображений
    group = models.ForeignKey(  # Внешний ключ на модель Group (группа, к которой принадлежит пост)
        Group, on_delete=models.CASCADE, related_name='posts',
        null=True, blank=True)  # Поле группы необязательно, если не указано, пост не привязан к группе

    def __str__(self):
        return self.text  # Возвращаем текст поста в виде строки (для удобства отображения)

# Модель для комментария
class Comment(models.Model):
    author = models.ForeignKey(  # Внешний ключ на модель User (автор комментария)
        User, on_delete=models.CASCADE, related_name='comments')  # Если пользователь удаляется, удаляются все его комментарии
    post = models.ForeignKey(  # Внешний ключ на модель Post (к какому посту относится комментарий)
        Post, on_delete=models.CASCADE, related_name='comments')  # Если пост удаляется, удаляются все комментарии к нему
    text = models.TextField()  # Текст комментария
    created = models.DateTimeField(  # Дата и время создания комментария
        'Дата добавления', auto_now_add=True, db_index=True)  # Дата добавления автоматически проставляется при создании комментария

# Модель для подписки
class Follow(models.Model):
    user = models.ForeignKey(  # Внешний ключ на модель User (пользователь, который подписывается)
        User,
        on_delete=models.CASCADE,
        related_name='follower')  # Если пользователь удаляется, удаляются все его подписки
    following = models.ForeignKey(  # Внешний ключ на модель User (пользователь, на которого подписываются)
        User,
        on_delete=models.CASCADE,
        related_name='following')  # Если пользователь удаляется, удаляются все его подписчики
