from rest_framework import serializers
from apps.common.models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):

  #Authorable
  # author
  authored_at = serializers.DateTimeField()

  #Timestampable
  created_at      = serializers.DateTimeField(read_only=True)
  modified_at     = serializers.DateTimeField(read_only=True)


  class Meta:
    model = Note
    fields = ('url',
              'text',
              'author', 'authored_at',
              'created_at', 'modified_at')
