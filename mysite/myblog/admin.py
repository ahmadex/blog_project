from django.contrib import admin
from myblog.models import Post, Comment, Visitor

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Visitor)
