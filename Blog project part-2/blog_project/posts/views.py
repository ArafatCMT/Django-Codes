from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('profile')
    else:
        post_form = PostForm()
    return render(request, 'add_post.html', {'form': post_form})

@login_required
def edit_post(request, id):
    post = Post.objects.get(pk = id)
    edit_post = PostForm(instance=post) 
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('profile')
    
    return render(request, 'add_post.html', {'form': edit_post})

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk = id).delete()
    return redirect('profile')
    
    
