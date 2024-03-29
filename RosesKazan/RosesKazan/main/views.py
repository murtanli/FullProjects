from django.shortcuts import render
from .forms import *

def main_page(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            return render(request, "main.html", {'result': query})
        else:
            form = SearchForm()
    return render(request, "main.html", {'form': form})

