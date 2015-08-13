from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.reverse import reverse

# from apps.store.views import api_root as store_api_root
# from apps.store.views.store import StoreList, StoreDetail
from apps.common.views import user, group, address
from apps.store.views import product, store


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet)
router.register(r'groups', group.GroupViewSet)
router.register(r'addresses', address.AddressViewSet)
router.register(r'stores', store.StoreViewSet)
router.register(r'products', product.ProductViewSet)


# Wire up our API using automatic URL routing.
urlpatterns = [
  url(r'^', include(router.urls)),

  # url(r'^stores/$', StoreList.as_view(), name='store-list'),
  # url(r'^stores/(?P<pk>[0-9]+)/$', StoreDetail.as_view(), name='store-detail'),

  # url(r'^products/$', ProductList.as_view(), name='product-list'),
  # url(r'^products/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name='product-detail'),

]

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]