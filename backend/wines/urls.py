from django.urls import path
from .views import wine_list

urlpatterns = [
    path("", wine_list, name="wine_list"),
]
