
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import models
from . import permissions
from . import serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'bio', 'web', 'full_name',)


class CurrentUserView(APIView):
    """get information of current user"""

    def get(self, request):
        serializer = serializers.UserProfileSerializer(request.user)
        return Response(serializer.data)

# class LoginViewSet(viewsets.ViewSet):
#     """Checks email and password and returns an auth token."""
#
#     serializer_class = AuthTokenSerializer
#
#     def create(self, request):
#         """Use the ObtainAuthToken APIView to validate and create a token"""
#
#         return ObtainAuthToken().post(request)

