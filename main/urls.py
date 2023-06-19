from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import home, post_detail, post_create
from .views import PostList, PostDetail, PostCreate, PostUpdate, APIPostsViewSet, post_detail

# api_detail_posts, APIPosts, APIDetailPosts

router = DefaultRouter()
router.register('posts', APIPostsViewSet)

urlpatterns = [
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('', PostList.as_view(), name='home'),
    # path('api/posts/<int:pk>', api_detail_posts, name='api_detail_posts'),
    # path('api/posts', APIPosts.as_view(), name='api_posts'),
    # path('api/posts/<int:pk>', APIDetailPosts.as_view(), name='api_posts_upd'),
    path('api/', include(router.urls)),
    path('comments/<int:pk>', post_detail, name='comments')]
