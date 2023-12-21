from django.contrib import admin
from proyecto_app.models import Alumnos, Institucion

class AlumnosAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(Alumnos, AlumnosAdmin)    


class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['nombre']

admin.site.register(Institucion, AlumnosAdmin)
# Register your models here.
