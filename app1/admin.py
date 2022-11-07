from django.contrib import admin

# Register your models here.
# username: admin
# password: social@123

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, uploaded_files

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "fullname", "username", "address", "public_visibility"]

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(uploaded_files)