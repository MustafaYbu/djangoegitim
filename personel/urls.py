from . import views
from django.urls import path,include
from personel.views import PersonelListView,PersonelDetailView

urlpatterns = [
   #path('', views.personeller,name="personeller"),
   path('',PersonelListView.as_view(),name="personel"),
   path('personeldetail/<int:pk>',PersonelDetailView.as_view(),name="personeldetay"),
   # path('<slug:category_slug>/<int:course_id>',views.course_detail,name="course_detail"),
    
   
     
]