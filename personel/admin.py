from django.contrib import admin
from .models import Personel

@admin.register(Personel)
class PersonelAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_filter=('name',)
    search_fields=('name','description')
