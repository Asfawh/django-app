from django.contrib import admin

# Register your models here.
from blogging.models import Post

# add a new admin registration
admin.site.register(Post)