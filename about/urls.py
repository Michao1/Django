from django.urls import path

from . import views

urlpatterns = [
    path('about/',views.about, name='about_index'),
    path('<int:pk>/', views.id_person, name='detail_about')
]
