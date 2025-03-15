from django.contrib.auth import get_user_model  # Импортируем функцию для получения модели пользователя.
from rest_framework import serializers, validators  # Импортируем сериализаторы и валидаторы из Django REST framework.
from rest_framework.relations import SlugRelatedField  # Импортируем тип поля для работы с внешними ключами, представленными через slug.
from posts.models import Comment, Post, Group, Follow  # Импортируем модели Post, Comment, Group и Follow для работы с ними.

# Сериализатор для модели Post (посты)
class PostSerializer(serializers.ModelSerializer):
    # Связь с автором поста, отображаем через поле 'username' (ссылка на модель пользователя через slug)
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        # Указываем модель, с которой работаем, и что нужно включить все поля
        fields = '__all__'  # Включаем все поля модели Post
        model = Post  # Указываем модель, с которой связан этот сериализатор

# Сериализатор для модели Comment (комментарии)
class CommentSerializer(serializers.ModelSerializer):
    # Связь с автором комментария, отображаем через поле 'username'
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        # Указываем модель и что все поля модели включаются в сериализованный объект
        fields = '__all__'  # Включаем все поля модели Comment
        read_only_fields = ('post',)  # Поле 'post' является только для чтения (поскольку комментарий не может быть изменен без поста)
        model = Comment  # Указываем модель Comment для сериализации

# Сериализатор для модели Group (группы)
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group  # Указываем модель Group для сериализации
        fields = ('id', 'title', 'slug', 'description')  # Указываем поля, которые включаются в сериализованный объект
        read_only_fields = ('id', 'title', 'slug', 'description')  # Эти поля доступны только для чтения, их нельзя изменять

# Сериализатор для модели Follow (подписки)
class FollowSerializer(serializers.ModelSerializer):
    # Поле 'user' (подписчик), получаем через slug (по имени пользователя) и указываем текущего пользователя по умолчанию
    user = serializers.SlugRelatedField(
        slug_field='username',  # Преобразуем пользователя в его имя (username)
        queryset=get_user_model().objects.all(),  # Получаем все объекты пользователя
        default=serializers.CurrentUserDefault()  # Устанавливаем текущего пользователя как значение по умолчанию
    )
    
    # Поле 'following' (на кого подписан пользователь), тоже получаем через slug
    following = serializers.SlugRelatedField(
        slug_field='username',  # Преобразуем подписанного пользователя в его имя
        queryset=get_user_model().objects.all()  # Получаем все объекты пользователя
    )

    class Meta:
        model = Follow  # Указываем модель Follow для сериализации
        fields = ('user', 'following')  # Включаем поля user и following
        validators = (
            validators.UniqueTogetherValidator(  # Добавляем уникальность подписки для каждой пары user-following
                queryset=Follow.objects.all(),
                fields=('user', 'following'),  # Пара для уникальности: пользователь и на кого подписан
                message=('Подписка уже существует')  # Сообщение, если подписка уже существует
            ),
        )

    # Метод для валидации данных
    def validate(self, data):
        # Проверка, чтобы пользователь не подписывался на самого себя
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Попытка подписаться на себя же'  # Сообщение ошибки, если пользователь пытается подписаться на себя
            )
        return data  # Возвращаем данные, если все проверки пройдены
