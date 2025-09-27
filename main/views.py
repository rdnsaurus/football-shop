import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ItemsEntryForm
from main.models import Items
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Items.objects.all()
    
    context = {
        'items': items,
        'last_login': request.COOKIES.get('last_login'),
        'user': request.user,
    }
    
    return render(request, 'main.html', context)

@login_required(login_url='/login')
def create_item(request):
    form = ItemsEntryForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        items_entry = form.save(commit=False)
        items_entry.user = request.user
        items_entry.save()
        return redirect('main:show_main')
    
    context = {
        'form': form,
    }
    return render(request, 'create_item.html', context)

@login_required(login_url='/login')
def see_details(request, id):
    item = get_object_or_404(Items, pk=id)

    context = {
        'item': item,
        'user': request.user,
        'access': item.user == request.user,
    }
    return render(request, 'details.html', context)

@login_required(login_url='/login')
def show_xml(request):
     items_list = Items.objects.all()
     xml_data = serializers.serialize("xml", items_list)
     return HttpResponse(xml_data, content_type="application/xml")

@login_required(login_url='/login')
def show_json(request):
    items_list = Items.objects.all()
    json_data = serializers.serialize("json", items_list)
    return HttpResponse(json_data, content_type="application/json")

@login_required(login_url='/login')
def show_xml_by_id(request, items_id):
   try:
       items_item = Items.objects.filter(pk=items_id)
       xml_data = serializers.serialize("xml", items_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Items.DoesNotExist:
       return HttpResponse(status=404)

@login_required(login_url='/login')
def show_json_by_id(request, items_id):
   try:
       items_item = Items.objects.get(pk=items_id)
       json_data = serializers.serialize("json", [items_item])
       return HttpResponse(json_data, content_type="application/json")
   except Items.DoesNotExist:
       return HttpResponse(status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = AuthenticationForm(request)
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def delete_item(request, id):
    item = get_object_or_404(Items, pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def edit_item(request, id):
    item = get_object_or_404(Items, pk=id)
    form = ItemsEntryForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'edit_item.html', context)