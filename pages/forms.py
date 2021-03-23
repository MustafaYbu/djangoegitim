from django import forms
from .models import Contact

class contactform(forms.ModelForm):
    ad=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Adinizi giriniz'
    
    
    
    }
    
    ))
    soyad=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Soyadinizi giriniz'
    
    
    
    }
    
    ))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
    'class':'form-control',
    'placeholder':'Email Adresinizi giriniz'
    
    
    
    }
    
    ))
    phone=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Telefon giriniz'
    
    
    
    }
    
    ))
    mesaj=forms.CharField(widget=forms.Textarea(attrs={
    'class':'form-control',
    'placeholder':'Adinizi giriniz'
    
    
    
    }
    
    ))

    class Meta:
        model=Contact
        fields=['ad','soyad','email','phone','mesaj']
