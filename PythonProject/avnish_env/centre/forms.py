from django import forms
from .models import alumne, professor  # Asegúrate de importar los modelos

class alumne_form(forms.ModelForm):
    class Meta:
        model = alumne
        fields = '__all__'  # Muestra todos los campos del modelo

class professor_form(forms.ModelForm):
    class Meta:
        model = professor
        fields = '__all__'  # Muestra todos los campos del modelo
