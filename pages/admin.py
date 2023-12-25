from django.contrib import admin

from .models import ScrollModel, GallaryModel, MenuModel, CategoryModel, RegistrationModel


@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(GallaryModel)
class GallaryModelAdmin(admin.ModelAdmin):
    list_display = ['id','created_at']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category' , 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'description']
    ordering = ['-created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    ordering = ['-created_at']


@admin.register(RegistrationModel)
class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'time', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'email']
    ordering = ['-created_at']