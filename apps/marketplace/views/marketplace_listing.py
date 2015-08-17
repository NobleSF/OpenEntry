from rest_framework import viewsets

from apps.marketplace.models import MarketplaceListing
from apps.marketplace.serializers.marketplace_listing import MarketplaceListingSerializer


class MarketplaceListingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = MarketplaceListing.objects.all()
    serializer_class = MarketplaceListingSerializer
