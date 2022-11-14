from django.db import models

# Create your models here.

class Marca(models.Model):
    marca_nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.marca_nombre

class Producto(models.Model):
    producto_nombre = models.CharField(max_length=50)
    producto_description = models.TextField()
    producto_precio = models.PositiveIntegerField(default=0)
    producto_cantidad = models.PositiveIntegerField()
    producto_marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    producto_imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.producto_nombre

opciones_tipo = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"suguerencia"],
    [3,"felicitaciones"],
]

class Contacto(models.Model):
    contacto_nombre = models.CharField(max_length=50)
    contacto_correo = models.EmailField()
    contacto_tipo = models.IntegerField(choices=opciones_tipo)
    contacto_mensaje = models.TextField()
    contacto_avisos = models.BooleanField()

    def __str__(self):
        return self.contacto_nombre