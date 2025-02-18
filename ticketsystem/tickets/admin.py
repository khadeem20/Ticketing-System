from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Ticket, Comment


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'role']
    search_fields = ['username', 'first_name', 'last_name', 'role']

#Register our models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Ticket)
admin.site.register(Comment)