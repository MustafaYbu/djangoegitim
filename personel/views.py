from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from personel.models import Personel
from courses.models import Course

class PersonelListView(ListView):
    
    model = Personel 
    #hangi model oldu[u belirtildi
    # paginate_by = 100  # if pagination is desired
    template_name='personel.html'
    #yonlendirilecek template belirtildi
    context_object_name='personellistesi'
    #personel html sayfasinda object olarak belirtilen  context olarak gonderilen degerdir.
    #queryset ile listview gounumu degistirile bilir
    #queryset=Personel.objects.all()[:2]
    #asagidaki listview sayfalaasi icin  kullaniliyor ve html kismindada html satirlari eklenecektir unutmayiniz
    paginate_by = 3 ## listviewde gisterilecek olan personel sayisini belirler


class PersonelDetailView(DetailView):
    
    model = Personel 
  
    template_name='personeldetay.html'
    context_object_name='cagrilanpersonel' 

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['verilendersler'] = Course.objects.all()
       
        context['verilendersler'] = Course.objects.filter(available=True, personel=self.kwargs['pk'])
       
        return context
        #sarta bagli olarak primaykey den hoca bulunup dersler cagrilacak
        
        #get context data farkli bir tablo ili iliskili olan verileri ayni objext icine almaya yarara
#html tarafinda kullanilacak objenin ismi belirlendi
  
    
    

# Create your views here.
