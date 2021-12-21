from django.urls import path
from blog_app.api.views import BlogPostListAPIView, BlogPostDetailAPIView

urlpatterns = [
    path('', BlogPostListAPIView.as_view()),
    path('post/<int:pk>/', BlogPostDetailAPIView.as_view())
]
