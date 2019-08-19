from django.contrib import admin
from .models import SteamApp, Category, Document, Comment

class SteamAppAdmin(admin.ModelAdmin):
    list_display = ['id', 'appid', 'name', 'final_price', 'coming_soon', 'release_date']

admin.site.register(SteamApp, SteamAppAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

# 관리자 페이지에서 댓글을 Document에서 편하게 관리하기 위해 추가
class CommentInline(admin.TabularInline):
    model = Comment

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['doc_sort', 'id', 'author', 'title', 'slug', 'create_date', 'update_date']
    prepopulated_fields = {'slug':('title',)}
    inlines = [CommentInline]

admin.site.register(Document, DocumentAdmin)
