from django.contrib import admin
from .models import Alumno, Docente, Aula, Periodo,  Curso, Notas, Asistencia, Estado_Asistencia

# Register your models here.
admin.site.register(Aula)
admin.site.register(Periodo)
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Docente)
admin.site.register(Notas)
admin.site.register(Asistencia)
admin.site.register(Estado_Asistencia)