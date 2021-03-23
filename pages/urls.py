

from . import views
from django.urls import path,include
from .views import AboutView,IndexView,ContactView

urlpatterns = [
   # path('', views.index,name="index"),
    #path('about/', views.about,name="about"),
    path('about/', AboutView.as_view(),name="about"),
   path('',IndexView.as_view(),name="index"),
   path('contact/', ContactView.as_view(),name="contact"),
     
]