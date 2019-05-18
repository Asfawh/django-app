from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category

# add a new admin registration
admin.site.register(Post)
admin.site.register(Category)