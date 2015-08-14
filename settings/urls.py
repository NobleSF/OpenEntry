from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.reverse import reverse

# from apps.store.views import api_root as store_api_root
# from apps.store.views.store import StoreList, StoreDetail
from apps.common.views import user, group, address, note
from apps.store.views import product, store


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

#common
router.register(r'users', user.UserViewSet)
router.register(r'groups', group.GroupViewSet)
router.register(r'addresses', address.AddressViewSet)
router.register(r'notes', note.NoteViewSet)

#store app
router.register(r'stores', store.StoreViewSet)
router.register(r'products', product.ProductViewSet)

#marketplace app





urlpatterns = [
  # Wire up our API using automatic URL routing.
  url(r'^api/', include(router.urls)),

  # Login and logout views for the browsable API
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
