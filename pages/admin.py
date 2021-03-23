from django.contrib import admin
from .models import Hakkimizda,Contact

@admin.register(Hakkimizda)
class HakkimizdaAdmin(admin.ModelAdmin):
    list_display=('baslik',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('ad','soyad')
      

