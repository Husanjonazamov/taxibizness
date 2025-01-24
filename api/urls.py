from django.urls import path
from .views import UserView, CategoryView, UserGetView



urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('users/<int:user_id>/', UserGetView.as_view(), name='usersget'),
    path('category/', CategoryView.as_view(), name='location'),
]
