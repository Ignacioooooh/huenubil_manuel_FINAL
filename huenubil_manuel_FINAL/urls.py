"""
URL configuration for huenubil_manuel_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listar/', views.listar_Inscripciones,name='listar'),
    path('agregar/', views.agregar_inscripcion,name='agregar'),
    path('agregar_institucion',views.agregar_instituciones),
    path('eliminar/<int:id>', views.eliminar_inscripcion,name='eliminar'),
    path('actualizar/<int:id>', views.actualizar_inscripcion,name='editar'),
    path('FBW/',views.InstitucionLista),
    path('FBW/<int:pk>',views.InstitucionDetalle),
    path('alumnos/', views.AlumnosLista.as_view()),
    path('ver/', views.verautor),
    path('alumnos/<int:pk>', views.AlumnosDetalle.as_view()),
]
