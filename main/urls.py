from django.urls import path

# from .views import home, post_detail, post_create
from .views import PostList, PostDetail, PostCreate, PostUpdate


urlpatterns = [
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('', PostList.as_view(), name='home'),
]