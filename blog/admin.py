from django.contrib import admin

from blog.models import *


# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name',)
    ordering = ('id',)



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # readnum是因为有外键关联，
    list_display = ('id', 'blog_type_id', 'title', 'auth', 'get_read_num', 'is_delete', 'create_time', 'update_time')


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'blog')
