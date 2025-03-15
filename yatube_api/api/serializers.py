from rest_framework import serializers
from .models import Post, Group, Comment, Follow
from django.contrib.auth import get_user_model

# Сериализатор для модели Post (посты)
class PostSerializer(serializers.ModelSerializer):
    # Сериализуем связанные объекты User и Group
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.SlugRelatedField(slug_field='title', queryset=Group.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ('id', 'text', 'created', 'author', 'group')  # Определяем поля, которые будут включены в сериализованный объект

# Сериализатор для модели Group (группы)
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')  # Поля для группы

# Сериализатор для модели Comment (комментарии)
class CommentSerializer(serializers.ModelSerializer):
    # Привязка комментария к автору
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'text', 'created', 'author', 'post')  # Определяем поля, которые будут включены в сериализованный объект

# Сериализатор для модели Follow (подписки)
class FollowSerializer(serializers.ModelSerializer):
    # Указываем авторов и пользователя, который подписан
    user = serializers.StringRelatedField(read_only=True)
    following = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')  # Поля для подписки

# Сериализатор для создания постов (посты без ID)
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('text', 'group')  # Только текст и группа

# Сериализатор для отображения информации о пользователях
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Используем стандартную модель пользователя Django
        fields = ('username', 'email', 'first_name', 'last_name')  # Поля пользователя
