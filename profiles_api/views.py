from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """ create a hello massage with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message })
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ handles a partial update of a object """
        """ Just only Some Fields"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'Method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewsets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return A hello Message """
        a_viewset = [
                'uses actions (list, create, retrieve, update, partial_update)',
                'Automatically maps to URLs using Routers',
                'Provides more Functionality with less code',
        ]
        return Response({'message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new Hello Message """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'hello {name}'
            return Response({'message':msg})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handles Getting An object by its id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """ Handles Updating An object by its id"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """ Handles Updating a part of An object by its id"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ Handles Destoying a part of An object by its id"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handles creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles Creating, reading and updating profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer): # is the django method
        """ sets the user profile to the logged in user """
        serializer.save(user_profile = self.request.user)
