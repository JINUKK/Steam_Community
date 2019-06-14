from django.contrib import admin
from .models import Category, Document

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'slug', 'create_date', 'update_date']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Document, DocumentAdmin)
