from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('userinfo', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    url('', include(router.urls))
]