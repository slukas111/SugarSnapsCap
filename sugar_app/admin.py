from django.contrib import admin
from .models import BoxItem, Categories

# Register your models here.

@admin.register(BoxItem)
class BoxItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'que_assign')

admin.site.register(Categories)
