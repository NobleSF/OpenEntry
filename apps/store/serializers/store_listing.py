from rest_framework import serializers
from apps.store.models import StoreListing


class StoreListingSerializer(serializers.HyperlinkedModelSerializer):

  #Timestampable
  created_at        = serializers.DateTimeField(read_only=True)
  modified_at       = serializers.DateTimeField(read_only=True)

  #Publishable
  published_at      = serializers.DateTimeField(required=False)
  unpublished_at    = serializers.DateTimeField(required=False)
  is_published      = serializers.BooleanField(read_only=True)

  #Expirable
  valid_at          = serializers.DateTimeField(required=False)
  expired_at        = serializers.DateTimeField(required=False)
  is_expired        = serializers.BooleanField(read_only=True)

  #Permalinkable
  slug              = serializers.SlugField(required=False)
  get_absolute_url  = serializers.CharField(read_only=True)

  class Meta:
    model = StoreListing
    fields = ('url',
              'store', 'product',
              'currency', 'retail_price', 'sale_price', 'wholesale_price',
              'title', 'description',

              'created_at', 'modified_at',
              'published_at', 'unpublished_at', 'is_published',
              'valid_at', 'expired_at', 'is_expired',
              'slug', 'get_absolute_url',
              )
