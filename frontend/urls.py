from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_page, name='user_page'),
]
