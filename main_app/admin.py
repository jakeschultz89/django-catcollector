from django.contrib import admin

# Import models
from .models import Cat, CatToy

# Register your models here.
admin.site.register(Cat)
admin.site.register(CatToy)