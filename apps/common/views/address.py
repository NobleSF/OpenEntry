from rest_framework import viewsets
from apps.common.models import Address
from apps.common.serializers.address import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
