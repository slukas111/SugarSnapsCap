from django.contrib import admin
from .models import BoxItem, Categories

# Register your models here.

@admin.register(BoxItem)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'location')
    list_editable = ('location',)

# admin.site.register(BoxItem)
admin.site.register(Categories)
