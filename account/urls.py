from django.urls import path, include
# from django.contrib.auth.views import LoginView, LogoutView

from .views import register, profile, ProfileUpdate


urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update')
]
