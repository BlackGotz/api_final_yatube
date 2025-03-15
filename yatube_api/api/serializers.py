from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model
from .models import Post, Comment, Group, Follow

User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Group.
    """
    class Meta:
        model = Group
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('pub_date',)

class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)

class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Follow.
    """
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        required=True
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Вы уже подписаны на этого пользователя.'
            )
        ]

    def validate_following(self, value):
        """
        Проверяет, что пользователь не подписывается сам на себя.
        """
        if self.context['request'].user == value:
            raise serializers.ValidationError('Нельзя подписаться на самого себя.')
        return value
