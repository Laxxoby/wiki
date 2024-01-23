from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.page, name="page"),
    path("wiki/search/<str:query>", views.search, name="search"),
    path("wiki/create/", views.create, name="create"),
    path("wiki/edit/<str:title>", views.edit, name="edit")
]
