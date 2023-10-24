from django.urls.conf import include, path
from pro14app import views

urlpatterns = [
    path('list', views.BuserFunc),
    path('jikwon', views.JikwonFunc),
    path('gogek', views.GogekFunc),
]