from django.shortcuts import render, redirect
from categoris.forms import CategoryForm

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        Category_form = CategoryForm(request.POST)
        if Category_form.is_valid():
            Category_form.save()
            return redirect('add_category')
    else:
        Category_form = CategoryForm()
    return render(request, 'add_category.html' , {'form': Category_form})
