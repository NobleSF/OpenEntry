from rest_framework import serializers, viewsets

from django.contrib.auth import get_user_model
UserModel = get_user_model()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = UserModel
    fields = ('url', 'username', 'email', 'password',
              'given_name', 'middle_name', 'surname')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
  queryset = UserModel.objects.all()
  serializer_class = UserSerializer
