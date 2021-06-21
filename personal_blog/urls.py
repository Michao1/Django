from django.urls import path 
from . import views

urlpatterns = [
    path("blog/", views.index_blog, name="index_blog"),
    path("<int:pk>/", views.detail_blog, name="detail_blog"),
    path("<category>/", views.category_blog, name="category_blog")
]
