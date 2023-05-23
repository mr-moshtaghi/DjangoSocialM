from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('person/<int:pk>/create-vacation/', views.create_vacation, name='create_vacation'),
]
