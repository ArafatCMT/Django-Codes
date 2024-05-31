from django.shortcuts import render, redirect
# from authors  import forms
from authors.forms  import AuthorForm
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            # print(author_form.cleaned_data)
            return redirect('add_author')
    else:
        author_form = AuthorForm()
    return render(request, 'add_author.html' , {'form': author_form})
