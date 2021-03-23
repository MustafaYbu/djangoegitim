

from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.courses,name="courses"),
    path('<slug:category_slug>/<int:course_id>',views.course_detail,name="course_detail"),
    path('categories/<slug:category_slug>',views.category_list,name="course_by_category"),
    # yukaridaki  kategporiye  bagli kurs sirlamasi yapacak olan function gider
    path('tags/<slug:tag_slug>',views.tag_list,name="course_by_tag"),
    path('kursarama/',views.arama,name="arama"),
    # yukaridaki  taga bagli kurs sirlamasi yapacak olan function gider

   
     
]