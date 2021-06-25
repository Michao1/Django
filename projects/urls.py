from django.urls import path

from .import views

urlpatterns = [
    path('projects/',views.index, name='index'),
    path('<int:pk>/', views.detail,name='detail')
]
