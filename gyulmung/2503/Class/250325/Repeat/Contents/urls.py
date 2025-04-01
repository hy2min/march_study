from django.urls import path
from . import views


app_name = 'Contents'
urlpatterns = [
    path('Samsung01/', views.index, name = 'index'),
    
]
