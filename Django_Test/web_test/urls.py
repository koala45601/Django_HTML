from django import urls
from django.urls import path,include
from web_test import views

urlpatterns = [
    # localhost:8000/
    path('#',views.homepage,name='home-page'),
    path('addstock/',views.addstock,name='add-stock'),
    path('stock_show/',views.show_stock, name='show-stock'),
    path('register_test1/',views.register, name='register_test'),
    path('search_1/',views.search_1, name='search-id'),    
    path('profile/',views.EditProfile, name='profile'),
    path('up_load_doc/',views.doc_upload, name='doc_up_load')
]
