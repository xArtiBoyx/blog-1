from django.urls import path, include
# from django.contrib.auth.views import LoginView, LogoutView

from .views import register, edit_profile, profile
# from .views import  profile_update

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    # path('profile/<int:pk>/update/', profile_update, name='profile_update')
    path('change_profile/', edit_profile, name='edit_profile')
]
