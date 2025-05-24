from django.urls import path
from .views import *

urlpatterns = [
  path('users/', get_users, name='get_users'),
  path('users/create/', create_user, name='create_user'),
   path('users/<int:pk>/', get_user_by_id),      # GET user by ID
    path('users/<int:pk>/update/', update_user),   # PUT
    path('users/<int:pk>/delete/', delete_user),   # DELETE
]