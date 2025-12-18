from django.urls import path
from .views import wine_list, recommend

urlpatterns = [
    path("", wine_list, name="wine_list"),
    path("recommend/", recommend, name="recommend"),
]
