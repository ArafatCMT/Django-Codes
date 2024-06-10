from django.shortcuts import render, redirect
from authors.forms  import RegistrationForm, ChangeUserData
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy



def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
    else:
        register_form = RegistrationForm()
    return render(request, './register_form.html' , {'form': register_form, 'type': 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_passwd = form.cleaned_data['password']
            user = authenticate(username= user_name, password= user_passwd)

            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login Information Incurrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, './register_form.html', {'form': form, 'type': 'Login'})

class UserLoginView(LoginView):
    template_name = 'register_form.html'

    def get_redirect_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in information incurrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

def user_logout(request):
    logout(request)
    return redirect('login')

class LogoutView(LogoutView):
    def get_redirect_url(self):
        messages.success(self.request, 'Logged Out Successful')
        return reverse_lazy('login')
    


@login_required
def profile(request):
    post  = Post.objects.filter(author = request.user)
    return render(request, './profile.html' ,{'data': post, 'owner_name': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserData(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = ChangeUserData(instance = request.user)
    return render(request, './update_profile.html', {'form': profile_form})

def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, './pass_change.html', {'form': form})
