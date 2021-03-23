from django.db import models
from personel.models import Personel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Category(models.Model):
    name=models.CharField(max_length=50,null=True,verbose_name="Kategori",help_text="Kategori adini giriniz")
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50,null=True,verbose_name="Tag",help_text="Tag adini giriniz")
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
class Course(models.Model):
    tag=models.ManyToManyField(Tag,blank=True,null=True)
    musteriler = models.ManyToManyField(User, blank=True, related_name='courses_joined')
    personel=models.ForeignKey(Personel,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,verbose_name="Kurs Adı",help_text="Kurs adini giriniz",unique=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    #description=models.(blank=True,null=True,verbose_name="Kurs Açıklaması")
    description=RichTextField()
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="courses/%y/%m/%d",default="courses/x.jpg")
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Firmalar(models.Model):
   
    name=models.CharField(max_length=20,verbose_name="Firma Adi",help_text="Firma adini giriniz",unique=True)
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="courses/%y/%m/%d",default="courses/x.jpg")
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create your models here.
