from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Paper, Figure, Entity

admin.site.register(Paper)
admin.site.register(Figure)
admin.site.register(Entity)
