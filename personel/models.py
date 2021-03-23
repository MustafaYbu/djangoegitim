from django.db import models
# Create your models here.
class Personel(models.Model):
    name=models.CharField(max_length=50)
    unvan=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    facebook=models.URLField(max_length=100,blank=True)
    instagram=models.URLField(max_length=100,blank=True)
    youtube=models.URLField(max_length=100,blank=True)
    image=models.ImageField(upload_to="courses/%y/%m/%d",default="courses/x.jpg")
    def __str__(self):
        return self.name
