from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    paginas = models.IntegerField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='libros/')
    
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    codido_estudiante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.libro.nombre