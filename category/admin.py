from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from .models import category, Users



@admin.register(category)
class LoctionAdmin(UnfoldModelAdmin):
    list_display = (
        'category',
        "__str__"
    )
    
@admin.register(Users)
class UserAdmin(UnfoldModelAdmin):
    list_display = (
        'firstname',
        'user_id',
        "__str__"
    )
    