# from rest_framework import status

from .models import Post
from .forms import PostForm
from .serializers import PostSerializer, PostDetailSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# def home(request):
#     # if request.user.is_authenticated:
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'main/home.html', {'posts': posts})
#
#
# def post_detail(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         pass
#     return render(request, 'main/post_detail.html', {'post': post})
#
# # def second_view(request):
# #     return render(request, 'main/second.html')
#
#
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             cd = form.save(commit=False)
#             cd.author = request.user
#             cd.save()
#             return redirect(home)
#     else:
#         form = PostForm()
#     return render(request, 'main/post_create.html', {'form': form})


class PostList(ListView):
    model = Post
    template_name = 'main/home.html'
    context_object_name = 'posts'
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admin_user'] = User.objects.get(id=1)
        return context


# def get_queryset(self):
#     return Post.objects.all().order_by('-created_at')


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    # model = Post
    form_class = PostForm
    template_name = 'main/post_create.html'
    success_url = '/blog/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/'
    pk_url_kwarg = 'pk'
    template_name = 'main/post_form.html'

    # def get_queryset(self):
    #     print(self.request.GET.get('pk'))
    #     return Post.objects.get(pk=self.request.GET.get('pk'))
    #
    # def get_object(self, queryset=None):
    #     inst = Post.objects.get(pk=self.kwargs.get('pk'))
    #     if self.request.user == inst.author:
    #         return inst


# @api_view(['GET'])
# def api_posts(request):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)


# class APIPosts(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class APIPosts(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class APIDetailPosts(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class APIPostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


@api_view(['GET'])
def api_detail_posts(request, pk):
    if request.method == "GET":
        posts = Post.objects.get(pk=pk)
        serializer = PostDetailSerializer(posts)
        return Response(serializer.data)
