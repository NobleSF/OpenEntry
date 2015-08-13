from rest_framework import viewsets
from django.contrib.auth import get_user_model
User = get_user_model()
from apps.common.serializers.user import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


