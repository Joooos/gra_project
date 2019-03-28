from django.contrib import admin
from .models import UserProfile, AuthUser

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(AuthUser)