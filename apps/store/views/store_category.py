from rest_framework import viewsets

from apps.store.models import StoreCategory
from apps.store.serializers.store_category import StoreCategorySerializer


class StoreCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer
