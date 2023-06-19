# from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from .serializers import PostDetailSerializer
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
        if 'counter' in self.request.session:
            self.request.session['counter'] += 1
            print(f'------------ counter={self.request.session["counter"]}')
        else:
            self.request.session['counter'] = 1
        return context

    # def render_to_response(self, context, **response_kwargs):
    #     response = super().render_to_response(context, **response_kwargs)
    #     if 'counter' in self.request.COOKIES:
    #         cnt = int(self.request.COOKIES.get('counter')) + 1
    #         response.set_cookie('counter', cnt)
    #         # print(f'====================== cnt: {cnt} type: {type: cnt}')
    #     else:
    #         response.set_cookie('counter', 1, max_age=5)
    #     return response


# def get_queryset(self):
#     return Post.objects.all().order_by('-created_at')

class PostDetail(DetailView):
    model = Post


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            form = CommentForm()
    return render(request, 'main/comments.html', {'post': post, 'comments': comments, 'form': form})


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


# def comments(request):
#     comment = Comment.objects.all()
#     form = CommentForm()
#     pk_url_kwarg = 'pk'
#     template_name = 'main/comments.html'
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = CommentForm()
#     return render(request, 'comments.html', {'comments': comment, 'form': form})


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
