from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps,AppConfig

from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Users


#from products.models import Product,StockPurchases,StockSales
class UsersAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    list_display = ["username","first_name","last_name","email","password"]


for model_name, model in apps.get_app_config('Users').models.items() :

    
    if      '_' not in model_name   :

        if      globals().get(model.__name__  +'Admin')   :     

            try:
                 admin.site.register(model, globals().get(model.__name__+'Admin'))
            except AlreadyRegistered:
                pass    
           
        else :

             try:
                 admin.site.register(model)
             except AlreadyRegistered:
                pass    
            