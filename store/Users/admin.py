from django.contrib import admin
from Users.models import User
from storeProducts.admin import BasketAdmin 

@admin.register(User) 
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff") 
    inlines = (BasketAdmin, )
