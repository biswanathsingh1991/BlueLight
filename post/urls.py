from django.urls import path
from . views import (HomeView, CreatePost, UpdatePost, ListPost,
                     DetailPostView, DeletePostView, post_comment_post)
from . import views

app_name = 'post'
urlpatterns = [

    path('home/', HomeView.as_view(), name='home'),
    path('createpost/', CreatePost.as_view(), name='createpost'),
    path('updatepost/<int:pk>/', UpdatePost.as_view(), name='updatepost'),
    path('listpost/', ListPost.as_view(), name='listpost'),
    path('detailpostview/<int:pk>/', DetailPostView.as_view(),
         name='detailpostview'),
    path('deletepost/<int:pk>/', DeletePostView.as_view(),
         name='deletepost'),
    path('testurl/', views.test, name='test'),
    path('post_comment_post/', post_comment_post, name='post_comment_post'),




]
