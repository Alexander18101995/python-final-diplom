"""orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include



from backend.views import RegisterAccount,LoginAccount,ShopView,CategoryView,ProductInfoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('shop', ShopView, basename='My')
router.register('category', CategoryView, basename='My')
router.register('productinfo', ProductInfoView, basename='My')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('api/',include(router.urls))
]
