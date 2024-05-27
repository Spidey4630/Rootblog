from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Blog/post_detail.html', {'post': post})

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        author = request.user
        comment = Comment(post=post, author=author, content=content)
        comment.save()
    return render(request, 'Blog/post_detail.html', {'post': post})
