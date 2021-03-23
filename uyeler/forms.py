from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Kullanici Adınız'  
    
    }
    
    ))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control',
    'placeholder':'Şİfrenizi giriniz'
    
    }
    
    ))
  

class Registerform(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Adiniz'  
    
    }
    
    ))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Soyadiniz'  
    
    }
    
    ))
    username=forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Kullanici Adiniz'  
    
    }
    
    ))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control',
    'placeholder':'Şİfrenizi giriniz'
    }
    
    ))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
    'class':'form-control',
    'placeholder':'şifreyi tekrar giriniz'
    
    }
    
    ))
    email=forms.CharField(widget=forms.EmailInput(attrs={
    'class':'form-control',
    'placeholder':'Email adresinizi Lutfen giriniz'
    
    
    
    }
    
    ))

class Meta:
        model=User
        fields=['first_name','last_name','email','password1','password2']
    
   