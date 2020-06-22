from django.db import models

# Create your models here.

class Alumno (models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    edad = models.IntegerField(blank = True)
    aula = models.ForeignKey('aula', on_delete = models.CASCADE)

    def __str__(self):
        return self.aula.grado + ' ' + self.aula.nivel + ' '+ self.nombre + ' ' + self.apellido 
    
    class Meta:
        db_table = 'educa_alumno'
        ordering = ['id']
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'

class Periodo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_periodo = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre_periodo
    
class Curso(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_curso = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nombre_curso']

    def __str__(self):
        return self.nombre_curso 

class Aula (models.Model):
    id = models.AutoField(primary_key = True)
    grado = models.CharField(max_length = 10)
    nivel = models.CharField(max_length = 50)
    cursos = models.ManyToManyField(Curso)
    

    def __str__(self):
        return self.grado + ' ' + self.nivel
    
    class Meta:
        db_table = 'educa_aula'
        ordering = ['id']
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'

class Docente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_docente = models.CharField(max_length=200, blank=False, null=False)
    apellido_docente = models.CharField(max_length=200, blank=False, null=False)
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return self.nombre_docente + ' ' + self.apellido_docente


class Notas(models.Model):
    id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey('Alumno', on_delete = models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE)
    aula= models.ForeignKey('Aula', on_delete = models.CASCADE, default = alumno)
    periodo = models.ForeignKey('Periodo', on_delete = models.CASCADE) 
    Nota = models.IntegerField(blank=False)

    def __str__(self):
        return self.alumno.nombre + ' ' + self.alumno.apellido + ' | ' + self.curso.nombre_curso + ' | ' + ' ' + str(self.Nota)

class Estado_Asistencia(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20,blank =True, null = True)

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    alumno = models.ForeignKey('Alumno', on_delete = models.CASCADE)
    fecha = models.DateTimeField(blank=False, null=False)
    curso = models.ForeignKey('Curso', on_delete = models.CASCADE)
    estado_asistencia = models.ForeignKey('Estado_Asistencia', on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.alumno.nombre + ' ' + self.alumno.apellido + ' ' + str(self.fecha) + ' ' + self.curso.nombre_curso