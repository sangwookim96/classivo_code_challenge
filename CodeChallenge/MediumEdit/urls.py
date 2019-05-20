from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='MediumEdit-home'),
    path('about/', views.about, name='MediumEdit-about'),
]
