from rest_framework import serializers
from apps.marketplace.models import Marketplace
from apps.store.models import Store

class MarketplaceSerializer(serializers.HyperlinkedModelSerializer):

  #Timestampable
  created_at        = serializers.DateTimeField(read_only=True)
  modified_at       = serializers.DateTimeField(read_only=True)

  #Publishable
  published_at      = serializers.DateTimeField(required=False)
  unpublished_at    = serializers.DateTimeField(required=False)
  is_published      = serializers.BooleanField(read_only=True)

  #Permalinkable
  slug              = serializers.SlugField(required=False)
  get_absolute_url  = serializers.CharField(read_only=True)

  #Annotatable
  #notes = M2M with Notes

  class Meta:
    model = Marketplace
    fields = ('url',
              'name', 'subdomain', 'domain',
              'default_currency',

              'created_at', 'modified_at',
              'published_at', 'unpublished_at', 'is_published',
              'slug', 'get_absolute_url',
              'notes',

              #related GET only
              'listings', 'categories',
              )
