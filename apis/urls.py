from django.urls import path

from .views import (
    ListCharacter,
    DetailCharacter,
)

urlpatterns = [
    path("<int:pk>/", DetailCharacter.as_view(), name="api-detail"),
    path("<str:name>/", ListCharacter.as_view(), name="api-name-detail"),
    path("", ListCharacter.as_view(), name="api-list"),
]
