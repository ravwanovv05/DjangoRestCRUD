from rest_framework.serializers import ModelSerializer
from main.models.posts import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
