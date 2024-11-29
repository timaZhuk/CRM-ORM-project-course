from django.contrib import admin
from .models import Client, Comment, Todolist


# ---- Register your models here ----
admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(Todolist)

