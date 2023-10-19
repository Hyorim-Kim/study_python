from django.urls import path
from pro3app import views

urlpatterns = [
    path('insert', views.InsertFunc),
]