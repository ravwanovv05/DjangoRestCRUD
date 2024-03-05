from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models.posts import Post
from main.serializers.posts import PostSerializer


class CreatePostGenericAPIView(GenericAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'message': 'Post successfully created'}, status=status.HTTP_201_CREATED)


class PostListGenericAPIView(GenericAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class PostUpdateGenericAPIView(GenericAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()

    def patch(self, request, post_id):
        post = Post.objects.get(id=post_id)
        serializer = self.get_serializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'message': 'Post successfully updated'}, status=status.HTTP_200_OK)


class PostDeleteAPIView(APIView):

    def delete(self, request, post_id):
        post = Post.objects.filter(id=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
