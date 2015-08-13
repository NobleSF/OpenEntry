from apps.store.models import Store
from apps.store.serializers.store import StoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# class StoreList(APIView): # GET, POST
#   """
#   List all stores, or create a new store.
#   """
#   def get(self, request, format=None):
#     stores = Store.objects.all()
#     serializer = StoreSerializer(stores, many=True)
#     return Response(serializer.data)
#
#   def post(self, request, format=None):
#     serializer = StoreSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class StoreDetail(APIView): # GET, PUT, DELETE
#   """
#   Retrieve, update or delete a store instance.
#   """
#   def get_object(self, pk):
#     try:
#       return Store.objects.get(pk=pk)
#     except Store.DoesNotExist:
#       raise Http404
#
#   def get(self, request, pk, format=None):
#     store = self.get_object(pk)
#     serializer = StoreSerializer(store)
#     return Response(serializer.data)
#
#   def put(self, request, pk, format=None):
#     store = self.get_object(pk)
#     serializer = StoreSerializer(store, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#   def delete(self, request, pk, format=None):
#     store = self.get_object(pk)
#     store.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import generics
#
# class StoreList(generics.ListCreateAPIView): # GET, POST
#   queryset = Store.objects.all()
#   serializer_class = StoreSerializer
#
# class StoreDetail(generics.RetrieveUpdateDestroyAPIView): # GET, PUT, DELETE
#   queryset = Store.objects.all()
#   serializer_class = StoreSerializer


from rest_framework import viewsets

class StoreViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides
  `list`, `create`, `retrieve`, `update` and `destroy` actions.
  """
  queryset = Store.objects.all()
  serializer_class = StoreSerializer
