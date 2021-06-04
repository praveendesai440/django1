from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home-page'),
    path('base/', views.base , name='base-page'),
    path('course/', views.course , name='course-page'),
    path('about/', views.about , name='about-page'),
]