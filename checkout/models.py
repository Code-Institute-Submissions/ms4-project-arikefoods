from django.db import models
from menu.models import Menu

""" Credits to Code Institute Boutique Ado Tutorial"""


class OrderDetails(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def __str__(self):
        return "{0}-{1}".format(self.id, self.full_name)


class OrderLineItem(models.Model):
    order_details = models.ForeignKey(OrderDetails, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    menu = models.ForeignKey(Menu, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.menu.name, self.menu.price)