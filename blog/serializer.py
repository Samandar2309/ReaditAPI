from rest_framework import serializers
from .models import Category, Tag, Author, Post, About, Clients, Comments, Info


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'tag', 'author', 'category', 'comment']
        read_only_fields = ['created_at', 'updated_at']
