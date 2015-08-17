from rest_framework import viewsets

from apps.marketplace.models import MarketplaceCategory
from apps.marketplace.serializers.marketplace_category import MarketplaceCategorySerializer


class MarketplaceCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = MarketplaceCategory.objects.all()
    serializer_class = MarketplaceCategorySerializer
