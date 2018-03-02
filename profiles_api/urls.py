from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views

router = DefaultRouter()
#router = routers.SimpleRouter()
router.register('userinfo', views.UserProfileViewSet)

urlpatterns = [
    url('', include(router.urls)),
    path('current-user/', views.CurrentUserView.as_view())
]