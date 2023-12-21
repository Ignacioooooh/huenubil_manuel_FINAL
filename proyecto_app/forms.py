from django import forms
from proyecto_app.models import Alumnos, Institucion

class FormAlumnos(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'


class FormInstituciones(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'