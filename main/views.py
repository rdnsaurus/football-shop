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
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Items.objects.all()
    form = ItemsEntryForm()
    
    context = {
        'items': items,
        'last_login': request.COOKIES.get('last_login'),
        'form' : form,
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
    item_list = Items.objects.all()
    data = [
        {
            'id': str(item.id),
            'name':item.name, 
            'price':item.price, 
            'description':item.description,
            'thumbnail':item.thumbnail, 
            'category':item.category, 
            'stock': item.stock,
        }
        for item in item_list
    ]

    return JsonResponse(data, safe=False)

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
        item = Items.objects.get(pk=items_id)
        data = [
        {
            'id': str(item.id),
            'name':item.name, 
            'price':item.price, 
            'description':item.description,
            'thumbnail':item.thumbnail if item.thumbnail else None, 
            'category':item.category, 
            'stock': item.stock,
            'user': item.user.username if item.user else None,
        }
    ]
        return JsonResponse(data, safe=False)
    except Items.DoesNotExist:
        return JsonResponse({'detail': 'Not Found'}, status=404)
   
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True, "message": "Register berhasil! Silakan login."})
            else:
                # fallback ke redirect biasa
                return redirect("main:login")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "message": "Form tidak valid. Coba lagi."})
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "message": "Login successful!"})
        else:
            return JsonResponse({"success": False, "message": "Invalid username or password."})
    
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
    try:
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")
        category = request.POST.get("category")
        stock = request.POST.get("stock")
        user = request.user

        print(f"Received: {name}, {price}, {description}")  # Debug

        new_item = Items(
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            stock=stock,
            user=user
        )
        new_item.save()
        print(f"Item saved with ID: {new_item.pk}")  # Debug

        return HttpResponse(b"CREATED", status=201)
    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse(str(e), status=400)

@login_required(login_url='/login')
def delete_item(request, id):
    item = get_object_or_404(Items, pk=id)
    item.delete()
    return JsonResponse({'status': 'success', 'message': 'Item deleted'}, status=200)

@csrf_exempt
@login_required(login_url='/login')
@require_POST
def edit_item(request, id):
    item = get_object_or_404(Items, pk=id, user=request.user)
    
    # Update fields
    item.name = request.POST.get('name')
    item.price = request.POST.get('price')
    item.description = request.POST.get('description')
    item.thumbnail = request.POST.get('thumbnail')
    item.category = request.POST.get('category')
    item.stock = request.POST.get('stock')
    
    item.save()
    
    return JsonResponse({'status': 'success', 'message': 'Item updated'}, status=200)