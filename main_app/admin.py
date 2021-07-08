from django.contrib import admin
# import your models here
from .models import Sales , Mod ,Genres

# Register your models here
admin.site.register(Sales)
admin.site.register(Mod)
admin.site.register(Genres)