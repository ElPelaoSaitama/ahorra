from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm

class ContactoFrom(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass