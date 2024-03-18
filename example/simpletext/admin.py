from .models import SimpleText, SimpleCategory
from django.contrib import admin

from categories.admin import CategoryBaseAdmin, CategoryBaseAdminForm


@admin.register(SimpleText)
class SimpleTextAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description', )
        }),
    )


class SimpleCategoryAdminForm(CategoryBaseAdminForm):
    class Meta:
        model = SimpleCategory
        fields = '__all__'


@admin.register(SimpleCategory)
class SimpleCategoryAdmin(CategoryBaseAdmin):
    form = SimpleCategoryAdminForm


