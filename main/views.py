from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
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

def see_details(request, id):
    item = get_object_or_404(Items, pk=id)

    context = {
        'item': item,
    }

    return render(request, 'details.html', context)

def show_xml(request):
     items_list = Items.objects.all()
     xml_data = serializers.serialize("xml", items_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items_list = Items.objects.all()
    json_data = serializers.serialize("json", items_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, items_id):
   try:
       items_item = Items.objects.filter(pk=items_id)
       xml_data = serializers.serialize("xml", items_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Items.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, items_id):
   try:
       items_item = Items.objects.get(pk=items_id)
       json_data = serializers.serialize("json", [items_item])
       return HttpResponse(json_data, content_type="application/json")
   except Items.DoesNotExist:
       return HttpResponse(status=404)