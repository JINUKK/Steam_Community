from django.contrib import admin
from .models import Category, Document, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

# 관리자 페이지에서 댓글을 Document에서 편하게 관리하기 위해 추가
class CommentInline(admin.TabularInline):
    model = Comment

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'slug', 'create_date', 'update_date']
    prepopulated_fields = {'slug':('title',)}
    inlines = [CommentInline]

admin.site.register(Document, DocumentAdmin)
