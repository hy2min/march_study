from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('samsung01', views.index, name='index')
]
