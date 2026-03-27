from django.db import models

# Create your models here.
class Producto(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=25)
    Cantidad=models.IntegerField()
    Precio=models.FloatField()
    Rareza=models.TextField(default="none")
    fechaIngreso=models.DateField()
    Imagen=models.ImageField(upload_to='Productos',null=True)
    
    def __int__(self):
       return self.Codigo