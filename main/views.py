from django.shortcuts import render, redirect
from main.forms import ItemsEntryForm
from main.models import Items

# Create your views here.

def show_main(request):
    items = Items.objects.all()
    
    context = {
        'items': items,
    }
    
    return render(request, 'main.html', context)

def create_item(request):
    form = ItemsEntryForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {
        'form': form,
    }
    return render(request, 'create_item.html', context)