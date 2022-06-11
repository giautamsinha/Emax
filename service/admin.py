from argparse import Action
from django.contrib import admin
from .models import Customer
from django.utils.html import format_html
# Register your models here.

class Cutomeradmin(admin.ModelAdmin):
    def upper_case_name(self,object):
        return("%s %s" % (object.first_name,object.last_name)).upper()
    upper_case_name.short_description='Name'
    def button(self,object):
        return format_html('<a href="test" class="link">Activate</a>',)
    button.short_description='Calender'
    
    list_display=('upper_case_name','address','phone','created_on','tiffin_start_date','button')
    search_fields=('first_name','last_name')
    action=[button]
    
admin.site.register(Customer,Cutomeradmin) 