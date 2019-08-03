"""ninegag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import UserRegistrationAPIView, UserLoginAPIView, GetToken, Logout
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

# Simple JWT TOKEN
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logiut/', Logout.as_view(), name='logout'),
    path('get-token/', GetToken.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('api/', include('post.urls')),

    # url Simple JWT TOKEN
    # url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]


# Theo cách này, Django sẽ chịu trách nhiệm phục vụ các tệp phương tiện trong quá trình phát triển (DEBUG = True).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)