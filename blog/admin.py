from django.contrib import admin
from blog.models import *
# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name',)
    ordering = ('id',)



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','blog_type_id','title','auth','is_delete','create_time','update_time')

