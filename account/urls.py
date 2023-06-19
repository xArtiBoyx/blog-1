from django.urls import path, include
# from django.contrib.auth.views import LoginView
from .views import register, edit_profile, profile, register_done
# from .views import  profile_update

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('profile/<int:pk>/update/', profile_update, name='profile_update'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('register/done/', register_done, name='register_done'),
    path('profile/', profile, name='profile'),
    path('change_profile/', edit_profile, name='edit_profile'),
]
