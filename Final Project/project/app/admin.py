from django.contrib import admin
from .models import *

class MemberAdmin(admin.ModelAdmin):
    list_display = ("user", "pasw", "email")

admin.site.register(Signup, MemberAdmin)

admin.site.register(Cakes)

admin.site.register(Cookies)

admin.site.register(Chaats)

admin.site.register(Order)

admin.site.register(Feedback)

# Register your models here.
