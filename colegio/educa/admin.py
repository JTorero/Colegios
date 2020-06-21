from django.contrib import admin
from .models import  Aula, Periodo, Aula_Periodo, Curso, Curso_docente, Notas, Asistencia, Aula_Curso_Docente

# Register your models here.
admin.site.register(Aula)
admin.site.register(Periodo)
admin.site.register(Aula_Periodo)
admin.site.register(Curso)
admin.site.register(Curso_docente)
admin.site.register(Notas)
admin.site.register(Asistencia)
admin.site.register(Aula_Curso_Docente)