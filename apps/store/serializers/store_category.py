from rest_framework import serializers

from apps.store.models import StoreCategory


class StoreCategorySerializer(serializers.HyperlinkedModelSerializer):

  #Timestampable
  created_at        = serializers.DateTimeField(read_only=True)
  modified_at       = serializers.DateTimeField(read_only=True)

  #Permalinkable
  slug              = serializers.SlugField(required=False)
  get_absolute_url  = serializers.CharField(read_only=True)

  class Meta:
    model = StoreCategory
    fields = ('url',
              'store', 'parent_category',
              'name', 'plural_name', 'keywords',
              #timestampable
              'created_at', 'modified_at',
              #permalinkable
              'slug', 'get_absolute_url',
              )
