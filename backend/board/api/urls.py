from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from board.api import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/replies/', views.ReplyList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
