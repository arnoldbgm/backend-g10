from django.db import models

# Create your models here.

class ProductosModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    precio = models.FloatField(null=False)
    estado = models.BooleanField(default=True, null=True)

    # Nombre de la tabla
    class Meta:
        db_table = 'productos'

    # Retornamos en un string el model
    # Señalamos que vamos a retornar
    def __str__(self) -> str:
        return self.nombre

    #! Null = False hace que sea obligatorio

class CategoriasModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    estado = models.BooleanField(default=True, null=True)
    # producto = models.ManyToManyField(ProductosModel)

    class Meta:
        db_table = 'categorias'
        
    def __str__(self) -> str:
        return self.nombre

class ProductosCategoriasModel(models.Model):
    id = models.AutoField(primary_key=True)
    producto_id = models.ForeignKey(ProductosModel, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(CategoriasModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'productos_categorias'