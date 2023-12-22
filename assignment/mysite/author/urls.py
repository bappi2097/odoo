from django.urls import path
from .views import (
    authorCreate,
    authorUpdate,
    authorDelete,
    authorList,
    authorDetails
)
from .apis import AuthorAPIView

urlpatterns = [
    path("", authorList, name="author-list"),
    path("<int:pk>/", authorDetails, name="author-detail"),
    path("create/", authorCreate, name="author-create"),
    path("<int:pk>/update/", authorUpdate, name="author-update"),
    path("<int:pk>/delete/", authorDelete, name="author-delete"),
    path('api/', AuthorAPIView.as_view(), name='author-api'),
    path('api/<int:author_id>/', AuthorAPIView.as_view(), name='author-api-detail'),
]
