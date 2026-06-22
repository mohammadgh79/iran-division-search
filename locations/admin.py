from django.contrib import admin
from .models import Division

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent','code']
    list_display_links=['name']
    search_fields=['name','code']
    list_filter=['parent']
