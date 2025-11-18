from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item/', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:items_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:items_id>/', show_json_by_id, name='show_json_by_id'),
    path('details/<str:id>/', see_details, name='see_details'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('edit/<uuid:id>/', edit_item, name='edit_item'),
    path('delete/<uuid:id>/', delete_item, name='delete_item'),
    path('create-ajax/', add_item_entry_ajax, name='add_item_entry_ajax'),
    path('create-flutter/', create_items_flutter, name='create_items_flutter'),
    path('proxy-image/', proxy_image, name='proxy_image'),  
]