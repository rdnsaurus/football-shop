from django.forms import ModelForm
from main.models import Items

class ItemsEntryForm(ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'price', 'description', 'thumbnail', 'category', 'stock']  