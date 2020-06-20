from django.contrib import admin
from .models import Alumno, Aula, Periodo, Aula_Periodo

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Aula)
admin.site.register(Periodo)
admin.site.register(Aula_Periodo)