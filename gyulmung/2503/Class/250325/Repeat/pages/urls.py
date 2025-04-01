from django.urls import path, include
from . import views

app_name = 'pages'
urlpatterns = [
    path('pages/<str:name>/', views.index, name='index')
]
