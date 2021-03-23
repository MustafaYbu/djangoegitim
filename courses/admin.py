from django.contrib import admin
from .models import Course,Category,Tag,Firmalar

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','available')
    list_filter=('available',)
    search_fields=('name','description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}#caktegory alanida slug alani otomatik dolsurulmasini daglar
#admin.site.register(Course)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}#tag alanida slug alani otomatik dolsurulmasini daglar
#admin.site.register(Course)
#admin.site.register(Category)
@admin.register(Firmalar)
class FirmaAdmin(admin.ModelAdmin):
    list_display=('name',)
    
# Register your models here.
