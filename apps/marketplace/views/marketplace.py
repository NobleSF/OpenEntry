from rest_framework import viewsets

from apps.marketplace.models import Marketplace
from apps.marketplace.serializers.marketplace import MarketplaceSerializer


class MarketplaceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Marketplace.objects.all()
    serializer_class = MarketplaceSerializer
