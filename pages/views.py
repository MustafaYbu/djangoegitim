from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from courses.models import Course,Firmalar
from django.views.generic.edit import FormView
from .forms import contactform
from django.urls import  reverse_lazy
from django.contrib.messages.views import  SuccessMessageMixin
from  personel.models import Personel
from 
from django.contrib.auth.models import User
# Create your views here.
#def index(request):
    #return HttpResponse("<h3> selam kanki </h3>")
 #return render(request,'index.html')

#def about(request):
    #return HttpResponse("<h3> selam kanki </h3>")
 #return render(request,'about.html')
class IndexView(TemplateView):#static sayfalarda yada biraz az deger gosterilen sayfalarda kullanilir
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kurslar'] = Course.objects.filter(available=True).order_by('-date')[:2]  # en son eklenen 2 deger anlamindadir sorgu#random.randrange(1, 100)
        context['toplamkurs']=Course.objects.filter(available=True).count() # toplam sayiyi belirtir
        context['firmalarimiz']=Firmalar.objects.all()
        context['personelsayimiz']=Personel.objects.all().count()
        return context

class AboutView(TemplateView):#static sayfalarda yada biraz az deger gosterilen sayfalarda kullanilir
    template_name='about.html'

class ContactView(SuccessMessageMixin,FormView):#form islemleri icin formview ile class olusturulur
    template_name='contact.html'
    form_class=contactform
    success_url=reverse_lazy('contact')
    success_message = " was created successfully"
#UNUTMADAN FORMDA MESAJ GOSTERMEK ICIN message import edilmelidir.

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)