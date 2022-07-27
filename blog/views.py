from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
from django.views import generic
# from django.urls import reverse_lazy

from .models import Post
from .forms import NewPostForm


# def post_list_view(request):
#     # all_post = Post.objects.all()
#     all_post = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/post_lists.html', {'all_post': all_post})


class PostListView(generic.ListView):
    # model = Post
    template_name = 'blog/post_lists.html'
    context_object_name = 'all_post'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     # post = None
#     return render(request, 'blog/post_detail.html', {'post': post})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form = NewPostForm()
#             return redirect('post_list')
#
#     else:  # Get request
#         form = NewPostForm()
#
#     return render(request, 'blog/post_create.html', context={'form': form})
#
#     # if request.method == 'POST':
#     #     post_title = request.POST.get('title')
#     #     post_text = request.POST.get('text')
#     #
#     #     user = User.objects.all()[0]
#     #     Post.objects.create(title=post_title, text=post_text,
#     #                         author=user, status='pub'
#     #                         )
#     #     all_post = Post.objects.filter(status='pub')
#     #     return render(request, 'blog/post_lists.html', {'all_post': all_post})
#     # else:
#     #     return render(request, 'blog/post_create.html')


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


def home_page(request):
    return render(request, 'blog/home.html')


# def post_update_view(request, pk):
#     # post = Post.objects.get(pk=pk)
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#     return render(request, 'blog/post_create.html', context={'form': form})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_delete.html', context={'post': post})


# class PostDeleteView(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_delete.html'
#     success_url = reverse_lazy('post_list')
