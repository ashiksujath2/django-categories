from django.contrib import admin

from categories.admin import CategoryBaseAdmin

from .models import SimpleCategory


@admin.register(SimpleCategory)
class SimpleCategoryAdmin(CategoryBaseAdmin):
    pass


