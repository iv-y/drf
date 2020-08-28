from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status, generics, permissions

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from django.db.models import Max

from board.models import Post, Reply
from board.api.serializers import PostSerializer, ReplySerializer, UserSerializer
from board.api.permissions import IsAuthorOrReadOnly, IsUserSelf

from board.api.helper import get_user_model


@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'users': reverse('user-list', request = request, format = format),
        'posts': reverse('post-list', request = request, format = format),
    })


class UserList(generics.ListAPIView):

    permission_classes = [
        permissions.IsAdminUser,
    ]

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):

    permission_classes = [
        permissions.IsAuthenticated,
        IsUserSelf,
    ]

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostList(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def get(self, request, format = None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        post_specific_data = {
            "author": request.user.id,
        }

        serializer = PostSerializer(data = {**request.data, **post_specific_data})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]

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


class ReplyList(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def get_post(self, pk):
        try:
            return Post.objects.get(pk = pk)
        except:
            raise Http404('No such post exist.')

    def get(self, request, pk, format = None):
        post = self.get_post(pk)
        replies = post.reply_set.order_by('reply_order').all()
        serializer = ReplySerializer(replies, many = True)

        return Response(serializer.data)

    def post(self, request, pk, format = None):
        post = self.get_post(pk)
        reply_specific_data = {
            "post": pk,
            "reply_order": post.reply_set.aggregate(Max('reply_order'))['reply_order__max'] + 1,
            "author": request.user.id,
        }
        serializer = ReplySerializer(data = {**request.data, **reply_specific_data})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# TODO Add a 'ReplyDetail' view