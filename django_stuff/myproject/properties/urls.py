from django.urls import path
from . import views

urlpatterns = [
	path('properties/', views.index, name = 'index')
]