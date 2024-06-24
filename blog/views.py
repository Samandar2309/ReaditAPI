from .serializer import *
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView


# Create your views here.

class HomeView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CommentsView(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class PostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('category')
        q = self.request.query_params.get('q')
        if tag:
            return Post.objects.filter(tags__name=tag)
        if category:
            return Post.objects.filter(categories__name=category)
        if q:
            return Post.objects.filter(title__icontains=q)
