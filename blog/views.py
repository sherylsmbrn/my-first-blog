from django.shortcuts import render, get_object_or_404
from .forms import PostForm
Post.objects.get(pk=pk)

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'templates/blog/post_list.html', {'post': post})