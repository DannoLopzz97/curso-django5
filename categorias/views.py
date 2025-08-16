from rest_framework.views import APIView
from django.http import JsonResponse
from http import HTTPStatus
from django.utils.text import slugify

from .models import Categoria
from .serializers import CategoriaSerializer

# Create your views here.
class CategoriaLista(APIView):
    def get(self, request):
        # listar todas las categorias 
        data = Categoria.objects.order_by('-id').all()
        serializer = CategoriaSerializer(data, many=True)
        return JsonResponse({"data":serializer.data}, status=HTTPStatus.OK)
    
    def post(self,request):
        # validar que la variable exista y no este vacia
        if request.data.get('nombre') is None or not request.data["nombre"]:
            return JsonResponse({"error":"El nombre es requerido"}, status=HTTPStatus.BAD_REQUEST)
        
        # crear la categoria
        try:
            Categoria.objects.create(
                nombre = request.data['nombre']
                )
            return JsonResponse({"mensaje":"Regstro agregado"}, status=HTTPStatus.CREATED)
        except Exception as e:
            return JsonResponse({"error":"Ocurrio un error inesperado"}, status=HTTPStatus.BAD_REQUEST)
    
    
class CategoriaDetalle(APIView):
    def get(self, request, id):
        try:
            data = Categoria.objects.get(id=id)
            serializer = CategoriaSerializer(data)
            return JsonResponse({"data":serializer.data}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            return JsonResponse({"error":"No existe la categoria"}, status=HTTPStatus.NOT_FOUND)
    
    def put(self, request, id):
        # validar que la variable exista y no este vacia
        if request.data.get('nombre') is None or not request.data["nombre"]:
            return JsonResponse({"error":"El nombre es requerido"}, status=HTTPStatus.BAD_REQUEST)
        
        # actualizar la categoria con el id proporcionado
        try:
            data = Categoria.objects.get(id=id)
            Categoria.objects.filter(id=id).update(
                nombre = request.data.get("nombre"),
                slug = slugify(request.data.get("nombre"))
            )
            return JsonResponse({"mensaje":"Regstro actualizado"}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            return JsonResponse({"error":"No existe la categoria"}, status=HTTPStatus.NOT_FOUND)
        
    def delete(self, request, id):
        # eliminar la categoria con el id proporcionado
        try:
            data = Categoria.objects.get(id=id)
            Categoria.objects.filter(id=id).delete()
            return JsonResponse({"mensaje":"Regstro eliminado"}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            return JsonResponse({"error":"No existe la categoria"}, status=HTTPStatus.NOT_FOUND)