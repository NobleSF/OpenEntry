from rest_framework import serializers
from apps.store.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Product
      fields = ('url', 'store', 'quantity', 'price')
