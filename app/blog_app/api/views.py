from blog_app.models import BlogPost
from blog_app.api.serializers import BlogPostListSerializer, BlogPostDetailSerializer
from rest_framework import generics


class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostListSerializer
        
    
class BlogPostDetailAPIView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostDetailSerializer
   