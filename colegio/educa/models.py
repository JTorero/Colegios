from django.db import models

# Create your models here.

class Aula (models.Model):
    id = models.AutoField(primary_key = True)
    grado = models.CharField(max_length = 10)
    nivel = models.CharField(max_length = 50)

    def __str__(self):
        return self.grado + ' ' + self.nivel
    
    class Meta:
        db_table = 'educa_aula'
        ordering = ['id']
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'

class Alumno (models.Model):
    id = models.AutoField(primary_key = True)
    aula = models.ForeignKey('Aula', on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 200)
    apellido = models.CharField(max_length = 200)
    edad = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Periodo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_periodo = models.CharField(max_length = 50)
    

    def __str__(self):
        return self.nombre_periodo
    
class Aula_Periodo(models.Model):
    id = models.AutoField(primary_key = True)
    aula = models.ForeignKey('Aula', on_delete = models.CASCADE)
    periodo = models.ForeignKey('Periodo', on_delete = models.CASCADE)

    def __str__(self):
        return self.aula.grado  + ' ' + self.aula.nivel + ' ' + self.periodo.nombre_periodo






