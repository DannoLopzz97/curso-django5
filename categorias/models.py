from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=1000, null=False, verbose_name='Nombre de la categoría')
    slug = AutoSlugField(populate_from='nombre')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categorias'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'