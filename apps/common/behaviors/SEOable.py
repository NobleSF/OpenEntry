from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class SEOable(models.Model):
  """
  page_title
  h1_title
  meta_description
  og_title
  og_description
  og_image
  og_upc
  og_availability

  derivative properties
  fb_app_id
  og_site_name
  og_type = 'product'
  og_price_amount = self.retail_price
  og_price_currency = self.product.currency.code
  og_url = self.get_absolute_url()
  og_product_price_amount = og_price_amount
  og_product_price_currency = og_price_currency
  og_product_shipping_cost_amount = self.default_shipping_cost
  og_product_shipping_cost_currency = og_price_currency
  """

  class Meta:
    abstract = True


@receiver(pre_save, sender=SEOable)
def pre_save(self, instance, *args, **kwargs):
  pass