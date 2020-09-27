from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.hey_there, name='home'),
    path("projects/", views.project_index, name="project"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('about/', views.about, name="about"),
    path('social/', views.social, name='social'),
    path('contact/', views.contact, name='contact'),
    path("blog/", include("blog.urls")),
    path('$/', views.project_detail, name='projects'),
]
