from django.urls import path
from .views import UserView, base_view

urlpatterns = [
    path('', base_view, name='base'),  # Base URL that shows the links
    path('users/', UserView.as_view(), name='users'),  # User API endpoint
]
