from django.db import models
from django.contrib.auth.models import Group
# Create your models here.

class Aula (models.Model):
    id = models.AutoField(primary_key = True)
    grado = models.CharField(max_length = 10)
    nivel = models.CharField(max_length = 50)

    def _str_(self):
        return self.grado + ' ' + self.nivel
    
    class Meta:
        db_table = 'educa_aula'
        ordering = ['id']
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'

class Periodo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_periodo = models.CharField(max_length = 50)

    def _str_(self):
        return self.nombre_periodo
    
class Aula_Periodo(models.Model):
    id = models.AutoField(primary_key = True)
    aula = models.ForeignKey('Aula', on_delete = models.CASCADE)
    periodo = models.ForeignKey('Periodo', on_delete = models.CASCADE)

    def _str_(self):
        return self.aula.grado  + ' ' + self.aula.nivel + ' ' + self.periodo.nombre_periodo

class Curso(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_curso = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nombre_curso']

    def _str_(self):
        return self.nombre_curso

class Curso_docente(models.Model):
    id = models.AutoField(primary_key = True)
    id_curso = models.ForeignKey('Curso', on_delete = models.CASCADE)
    docentes = models.ForeignKey('auth.user', on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Curso_Docente'
        verbose_name_plural = 'Cursos_Docentes'
        ordering = ['docentes']
        # users_in_group = Group.objects.get(name="Docente").user_set.all()
        # if user in users_in_group:
        #     print(user)

    def _str_(self):
        return self.id

class Aula_Curso_Docente(models.Model):
    id = models.AutoField(primary_key=True)
    aula = models.ForeignKey('Aula', on_delete=models.CASCADE)
    curso_docente_id = models.ForeignKey('Curso_Docente', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aula_Curso_Docente'
        verbose_name_plural = 'Aulas_Cursos_Docentes'
        ordering = ['id']

    def _str_(self):
        return self.id

class Notas(models.Model):
    alumno = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    id_curso = models.ForeignKey('Curso', on_delete = models.CASCADE)
    id_aula_periodo= models.ForeignKey('Aula_Periodo', on_delete = models.CASCADE)
    Nota = models.IntegerField(blank=False)


class Asistencia(models.Model):
    alumno = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    fecha = models.DateField(blank=False, null=False)
    id_curso_docente = models.ForeignKey('Curso_docente', on_delete = models.CASCADE)


 Entry.objects.filter(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')