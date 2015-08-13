from rest_framework import mixins
from rest_framework import generics

from apps.store.models.product import Product
from apps.store.serializers.product import ProductSerializer


# class ProductList(mixins.ListModelMixin,        # GET
#                   mixins.CreateModelMixin,      # POST
#                   generics.GenericAPIView):
#
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
#
#   def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)
#
#   def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)
#
#
# class ProductDetail(mixins.RetrieveModelMixin,  # GET
#                     mixins.UpdateModelMixin,    # PUT
#                     mixins.DestroyModelMixin,   # DELETE
#                     generics.GenericAPIView):
#
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
#
#   def get(self, request, *args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)
#
#   def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)
#
#   def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)
#


from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
