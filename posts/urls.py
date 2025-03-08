from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="home"),
    path("posts/", views.list_post, name="post_list"),
    path("posts/<int:id>/", views.list_post_detail, name="post_details"),
]