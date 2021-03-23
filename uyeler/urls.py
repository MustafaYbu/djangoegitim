from . import views
from django.urls import path,include


urlpatterns = [
   #path('', views.personeller,name="personeller"),
   path('login/',views.user_login,name="userlogin"),
   path('register/',views.user_register,name="userregister"),
    path('logout/',views.user_logout,name="userlogout"),
    path('dashboard/',views.user_dashboard,name="userdashboard"),
    path('kursakayitol/',views.kursakayitol,name="kursakayitol"),
  
   # path('<slug:category_slug>/<int:course_id>',views.course_detail,name="course_detail"),
    
   
     
]