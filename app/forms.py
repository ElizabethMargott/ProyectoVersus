from django import forms
from .models import *

class  AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__' 

class  EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__' 

class  LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__' 

class  EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__' 

class  PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__' 
