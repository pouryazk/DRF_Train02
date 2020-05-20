from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()


router.register('feed', views.UserProfileFeedViewSet)
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset') # // is not needed
router.register('profile', views.UserProfileViewSet) # // is not needed

""" if you define a query set, there is no need to define a basename,
 django Automatically assigns it from model name """

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
