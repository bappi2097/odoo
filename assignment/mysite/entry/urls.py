from django.urls import path
from .views import (
    EntryListView,
    EntryDetailView,
    EntryCreateView,
    EntryUpdateView,
    EntryDeleteView
)

urlpatterns = [
    path("", EntryListView.as_view(), name="entry-list"),
    path("<int:pk>/", EntryDetailView.as_view(), name="entry-detail"),
    path("create/", EntryCreateView.as_view(), name="entry-create"),
    path("<int:pk>/update/", EntryUpdateView.as_view(), name="entry-update"),
    path("<int:pk>/delete/", EntryDeleteView.as_view(), name="entry-delete"),
]
