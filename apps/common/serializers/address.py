from rest_framework import serializers
from apps.common.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
  created_at      = serializers.DateTimeField(read_only=True)
  modified_at     = serializers.DateTimeField(read_only=True)
  google_map_url  = serializers.URLField(read_only=True)

  class Meta:
    model = Address
    fields = ('url',
              'line_1', 'line_2', 'line_3',
              'city', 'region', 'postal_code', 'country',
              'created_at', 'modified_at',
              'google_map_url')
