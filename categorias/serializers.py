from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'slug']
        #read_only_fields = ['id', 'slug']  # slug is auto-generated, so it should be read-only