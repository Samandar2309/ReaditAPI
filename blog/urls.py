from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/', CategoryView.as_view(), name='category'),
    path('tag/', TagView.as_view(), name='tag'),
    path('author/', AuthorView.as_view(), name='author'),
    path('comments/', CommentsView.as_view(), name='comments'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),

]