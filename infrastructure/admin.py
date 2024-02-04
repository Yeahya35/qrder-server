from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(CustomUser, admin.ModelAdmin)
admin.site.register(Menu, admin.ModelAdmin)
admin.site.register(MenuItem, admin.ModelAdmin)
admin.site.register(Order, admin.ModelAdmin)
