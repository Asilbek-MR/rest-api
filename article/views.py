from .models import Article
from rest_framework import generics
from .serializers import ArticleSerializer


class ArticleListView(generics.ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class ArticleDetailView(generics.RetrieveAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer




