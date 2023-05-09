from django.contrib import admin
from .models import Category, ActivityCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'goal', 'color_code', 'created_at', 'updated_at', 'is_deleted')

admin.site.register(Category, CategoryAdmin)
admin.site.register(ActivityCategory)
