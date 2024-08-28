from rest_framework import serializers
from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    def create(self, validated_data):
        category_name = validated_data.pop('category')
        category = Category.objects.get(name=category_name)
        post = Post.objects.create(category=category, **validated_data)
        return post
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
