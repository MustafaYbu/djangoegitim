from django.db import models
# Create your models here.
class Hakkimizda(models.Model):
    baslik=models.CharField(max_length=50)    
    aciklama=models.TextField(blank=True)
    facebook=models.URLField(max_length=100,blank=True)
    instagram=models.URLField(max_length=100,blank=True)
    youtube=models.URLField(max_length=100,blank=True)
    image=models.ImageField(upload_to="courses/%y/%m/%d",default="courses/x.jpg")
    def __str__(self):
        return self.baslik

class Contact(models.Model):
    ad=models.CharField(max_length=50)  
    soyad=models.CharField(max_length=50)  
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=11)  
    mesaj=models.TextField(blank=True)

    def __str__(self):
        return self.ad