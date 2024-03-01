
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps,AppConfig

from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.utils.html import format_html

from .models import Book,BookClub,BookExchange,BookReview

class BookAdmin(admin.ModelAdmin):


    def image_tag(self, obj):
        #display image if it exists else return none
        return format_html('<img src="{}" width="100" height="100"  />'.format(obj.cover_image.url)) if obj.cover_image else None
    #mages
    image_tag.short_description = 'book  Image'




    list_display=['image_tag','format','name','author','publication_date','price']


class BookClubAdmin(admin.ModelAdmin):
    list_display=['name','owner','display_members']

    #list_display = ('get_products', 'vendor')

    def display_members(self, obj):
        """
        Custom function to display all members of the club in admin.
        """
        return ", ".join([member.username for member in obj.members.all()])

    display_members.short_description = 'Members'

class BookExchangeAdmin(admin.ModelAdmin):
    list_display=['book','borrower','date_borrowed','return_due_date','is_returned']


class BookReviewAdmin(admin.ModelAdmin):
    list_display=['book','user','rating','review_text']


for model_name, model in apps.get_app_config('books').models.items() :

    
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
            
