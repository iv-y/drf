from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

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
        'replies': reverse('reply-list', request = request, format = format),
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


class UserSelf(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class PostList(generics.ListCreateAPIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    queryset = Post.objects.__module__order_by('-id').all()
    serializer_class = PostSerializer
    filterset_fields = (
        'title',
        'content',
    )

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ReplyList(generics.ListCreateAPIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    filterset_fields = (
        'post',
        'content',
    )

    def perform_create(self, serializer):
        post = Post.objects.get(id = self.request.data["post"])
        reply_order = post.reply_set.aggregate(Max('reply_order'))['reply_order__max'] + 1

        serializer.save(author = self.request.user, reply_order = reply_order)


# TODO Add a 'ReplyDetail' view
