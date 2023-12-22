from django.urls import path
from .views import (
    blogList,
    blogDetail,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

from .apis import BlogAPIView

urlpatterns = [
    path("", blogList, name="blog-list"),
    path("<int:pk>/", blogDetail, name="blog-detail"),
    path("create/", BlogCreateView.as_view(), name="blog-create"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog-update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog-delete"),
    path('api/', BlogAPIView.as_view(), name='blog-api'),
    path('api/<int:blog_id>/', BlogAPIView.as_view(), name='blog-api-detail'),

]
