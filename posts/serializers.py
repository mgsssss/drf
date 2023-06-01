from rest_framework import serializers
from users.serializers import ProfileSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # nested serializer
    
    class Meta:
        model = Post
        fields = ["pk", "title", "body", "image", "published_data", "likes"]
        
class PostCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ["pk", "title", "body", "image"]