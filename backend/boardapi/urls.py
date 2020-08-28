from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('board.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),

    path('api/rest-auth/obtain-token/', obtain_jwt_token, name = 'obtain-jwt'),
    path('api/rest-auth/refresh-token/', refresh_jwt_token, name = 'refresh-jwt'),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
]
