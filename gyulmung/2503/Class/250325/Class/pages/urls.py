
from django.urls import path
from . import views

app_name= 'pages'

urlpatterns = [
    path('greeting/<str:name>/', views.index, name = 'index')

]
