from .models import *
from rest_framework import serializers

class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Categoria
        fields = '__all__'

class ProductoSerializers(serializers.ModelSerializer):
    producto_marca = serializers.CharField(read_only=True, source="producto_marca.marca_nombre")
    producto_marca = MarcaSerializers(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="producto_marca")
    producto_categoria = serializers.CharField(read_only=True, source="producto_categoria.categoria_nombre")
    producto_categoria = CategoriaSerializers(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="producto_categoria")



    class Meta:
        model = Producto
        fields = '__all__'