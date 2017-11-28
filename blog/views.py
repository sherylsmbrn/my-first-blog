from django.shortcuts import render, get_object_or_404
from .forms import PostForm
Post.objects.get(pk=pk)


def post_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'templates/blog/post_list.html', {'post': post})