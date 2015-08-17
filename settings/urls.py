from django.conf.urls import url, include
from rest_framework import routers

from apps.common.views import user, group, address, note
from apps.store.views import store, product, store_category, store_listing
from apps.marketplace.views import marketplace


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
router.register(r'store_listings', store_listing.StoreListingViewSet)
router.register(r'store_categories', store_category.StoreCategoryViewSet)

#marketplace app
router.register(r'marketplaces', marketplace.MarketplaceViewSet)




urlpatterns = [
  # Wire up our API using automatic URL routing.
  url(r'^api/', include(router.urls)),

  # Login and logout views for the browsable API
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^docs/', include('rest_framework_swagger.urls')),
]
