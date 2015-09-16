from rest_framework import serializers
from apps.store.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
  #Timestampable
  created_at      = serializers.DateTimeField(read_only=True)
  modified_at     = serializers.DateTimeField(read_only=True)

  class Meta:
    model = Product
    fields = ('url',
              'store', 'quantity',
              'name', 'description',
              'categories', 'colors',
              'width', 'height', 'length', 'weight',
              'currency', 'price',
              # 'shipping_options',
              'created_at', 'modified_at',
              )
