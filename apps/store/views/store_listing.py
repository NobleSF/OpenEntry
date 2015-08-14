from rest_framework import viewsets
from apps.store.models import StoreListing
from apps.store.serializers.store_listing import StoreListingSerializer


class StoreListingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = StoreListing.objects.all()
    serializer_class = StoreListingSerializer
