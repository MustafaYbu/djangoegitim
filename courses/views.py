from django.shortcuts import render
from .models import Course,Category,Tag

# Create your views here.
def courses(request):
    
    # siralama yapilmamai;tir kurslarimiz=Course.objects.all()
    kurslarimiz=Course.objects.all().order_by('-date')
    kategorilerimiz=Category.objects.all()
    taglarimiz=Tag.objects.all()
    context={
        'kurs':kurslarimiz,
        'kategori':kategorilerimiz,
        'taglarimiz':taglarimiz
    }
    return render(request,"courses.html",context)

def course_detail(request,category_slug,course_id):
        
    # siralama yapilmamai;tir kurslarimiz=Course.objects.all()
    kursumuz=Course.objects.get(category__slug=category_slug,id=course_id)
    context={
        'kurs':kursumuz
    }
    return render(request,"course.html",context)
def category_list(request,category_slug):
        
    # siralama yapilmamai;tir kurslarimiz=Course.objects.all()
    kursumuz=Course.objects.all().filter(category__slug=category_slug)
    kategorilerimiz=Category.objects.all()
    taglarimiz=Tag.objects.all()
    context={
        'kurs':kursumuz,
        'kategori':kategorilerimiz,
        'taglarimiz':taglarimiz
    }
    return render(request,"courses.html",context)

def tag_list(request,tag_slug):
        
    # siralama yapilmamai;tir kurslarimiz=Course.objects.all()
    kursumuz=Course.objects.all().filter(tag__slug=tag_slug)
    kategorilerimiz=Category.objects.all()
    taglarimiz=Tag.objects.all()
    context={
        'kurs':kursumuz,
        'kategori':kategorilerimiz,
        'taglarimiz':taglarimiz
    }
    return render(request,"courses.html",context)

def arama(request):
    kursumuz=Course.objects.filter(name__contains=request.GET['search'])
    kategorilerimiz=Category.objects.all()
    taglarimiz=Tag.objects.all()
    context={
        'kurs':kursumuz,
        'kategori':kategorilerimiz,
        'taglarimiz':taglarimiz
    }
    return render(request,"courses.html",context)