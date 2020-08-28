from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

from board.models import Post, Reply
from board.api.serializers import PostSerializer, ReplySerializer


class PostList(APIView):

    def get(self, request, format = None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk = pk)
        except:
            raise Http404('No such post exist.')

    def get(self, request, pk, format = None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        post = self.get_object(pk)
        post.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)


