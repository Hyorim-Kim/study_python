from django.urls import path
from pro11app import views


urlpatterns = [
    path('', views.ListFunc),
    path('insertok', views.InsertOkFunc),
]