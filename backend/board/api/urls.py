from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from board.api import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name = 'post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name = 'post-detail'),
    path('replies/', views.ReplyList.as_view(), name = 'reply-list'),

    path('users/', views.UserList.as_view(), name = 'user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user-detail'),

    path('userself/', views.UserSelf.as_view(), name = 'user-self'),

    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
