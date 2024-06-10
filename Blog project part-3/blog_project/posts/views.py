from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from posts.forms import PostForm, CommentForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator

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

# add post create class base view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk = id).delete()
    return redirect('profile')

@method_decorator(login_required, name= 'dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

class DetailsPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object() # post model object ta store kore raklam
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # post model object ta store kore raklam
        comments = post.comments.all()  # ei khan e ak ta post er moddhe joto comment ase sob store kora hocca
        comment_form = CommentForm()
            
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

    
    
