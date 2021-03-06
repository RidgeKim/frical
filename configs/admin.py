from django.contrib import admin
from .models import Config 

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('site', 'address', 'phone',)

    def has_add_permission(self, request):
        return False
