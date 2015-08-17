from rest_framework import serializers
from apps.store.models import Store

#
# class StoreSerializer(serializers.Serializer):
#   pk        = serializers.IntegerField(read_only=True)
#   name      = serializers.CharField(required=True, max_length=50)
#   subdomain = serializers.CharField(required=False, allow_blank=True, max_length=50)
#   domain    = serializers.CharField(required=False, allow_blank=True, max_length=100)
#
#   def create(self, validated_data):
#     """
#     Create and return a new `Store` instance, given the validated data.
#     """
#     return Store.objects.create(**validated_data)
#
#   def update(self, instance, validated_data):
#     """
#     Update and return an existing `Store` instance, given the validated data.
#     """
#     instance.name = validated_data.get('name', instance.name)
#     instance.subdomain = validated_data.get('subdomain', instance.subdomain)
#     instance.domain = validated_data.get('domain', instance.domain)
#     instance.save()
#     return instance

class StoreSerializer(serializers.HyperlinkedModelSerializer):

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

  class Meta:
    model = Store
    fields = ('url',
              'name', 'subdomain', 'domain',
              'default_currency',

              'created_at', 'modified_at',
              'published_at', 'unpublished_at', 'is_published',
              'slug', 'get_absolute_url',

              #related GET only
              'listings', 'categories', 'products',
              )
