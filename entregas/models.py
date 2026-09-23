from django.db import models

# Create your models here.
class Entrega(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_ruta', 'En ruta'),
        ('entregado', 'Entregado'),
    ]

    codigo = models.CharField(max_length=50)
    camion = models.CharField(max_length=20)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return self.codigo
