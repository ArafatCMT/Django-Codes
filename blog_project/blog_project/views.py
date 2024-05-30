from django.shortcuts import render
from posts.models import Post
def home(request):
    post = Post.objects.all()
    # print(post)
    return render(request, 'home.html', {'data': post})