from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductosModel, CategoriasModel, ClientesModel , OrdenesModel, DetallesOrdenModel
from .serializers import ProductosSerializer, CategoriasSerializer, ClientesSerializer, OrdenesSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from pprint import pprint
from django.contrib.auth.models import User
# Create your views here.

# Ejemplo base
def renderHtml(request):
    return HttpResponse("Texto cualquiera")

def buscarProducto(request, producto_id):
    producto = ProductosModel.objects.filter(id=producto_id).first()
    print(producto)
    return HttpResponse(f'Producto encontrado se llama {producto.nombre} ')
# Fin del ejemplo base

class ProductosView(generics.ListCreateAPIView):
    queryset = ProductosModel.objects.all()
    serializer_class = ProductosSerializer

class CategoriasView(generics.GenericAPIView):
    serializer_class = CategoriasSerializer
    queryset = CategoriasModel.objects.all()

    def get(self, request):
        try:
            record = self.get_queryset()
            serializer = self.get_serializer(record, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                data = {
                    'message': 'Internal server error',
                    'error': str(e)
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            categoria = self.get_serializer(data=request.data)
            if categoria.is_valid():
                categoria.save()
                return Response(categoria.data)

            error = 'Faltan campos'
            for campo in categoria.errors:
                error = error + ' ' + campo + ', '
            return Response({
                'message': error
            })
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ActualizarCategoriasView(generics.GenericAPIView):
    queryset = CategoriasModel.objects.all()
    serializer_class = CategoriasSerializer

    def get(self, request, categoria_id):
        try:
            record = self.get_queryset().get(id=categoria_id)
            serializer = self.get_serializer(record)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, categoria_id):
        try:
            categoria = self.get_queryset().get(id=categoria_id)
            serializer = self.get_serializer(categoria, data=request.data)
            if serializer.is_valid():
                categoria_actualizada = serializer.update(categoria, serializer.validated_data)
                nuevo_serializador = self.get_serializer(categoria_actualizada)
                return Response(nuevo_serializador.data, status=status.HTTP_201_CREATED)
                
            error = 'Faltan campos'
            for campo in categoria.errors:
                error = error + ' ' + campo + ', '
            return Response({
                'message': error
            })
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, categoria_id):
        try:
            categoria = self.get_queryset().get(id=categoria_id)
            serializador = self.get_serializer(categoria)
            serializador.delete()
            print(categoria)
            return Response({
                'message': 'Categoria eliminada'
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class OrdenesView(generics.GenericAPIView):
    queryset = OrdenesModel.objects.all()
    serializer_class = OrdenesSerializer

    def post(self, request):
        try:
            orden = self.get_serializer(data=request.data)
            if orden.is_valid():
                cliente = ClientesModel(**request.data['cliente'])
                cliente.save()

                usuario = User.objects.get(id=request.data['usuario_id'])
                orden_dict = {
                    'codigo': request.data['codigo'],
                    'observacion': request.data['observacion'],
                    'cliente_id': cliente,
                    'usuario_id': usuario
                }
                orden = OrdenesModel(**orden_dict)
                orden.save()

                for detalle in request.data['detalle']:
                    producto = ProductosModel.objects.get(id=detalle['producto_id'])
                    detalle_dict = {
                        'cantidad': detalle['cantidad'],
                        'producto_id': producto,
                        'orden_id': orden
                    }
                    detalle = DetallesOrdenModel(**detalle_dict)
                    detalle.save()
                return Response({
                    'message': 'Operacion exitosa'
                }, status=status.HTTP_201_CREATED)
            error = 'Faltan campos'
            for campo in orden.errors:
                error = error + ' ' + campo + ', '
            return Response({
                'message': error
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)