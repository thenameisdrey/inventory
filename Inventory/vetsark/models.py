from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
import uuid

# Create your models here.

class NewStock(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class StockDetails(models.Model):
    category = models.ForeignKey(NewStock, on_delete=models.CASCADE)
    name_of_item = models.CharField(max_length=50)
    qty_at_hand = models.DecimalField(max_digits=19, decimal_places=2)
    cost_price = models.DecimalField(max_digits=19, decimal_places=2)
    sales_price = models.DecimalField(max_digits=19, decimal_places=2)
    re_order = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name_of_item

class CustomersDetails(models.Model):
    customer_name = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=150, blank=False)
    email = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    opening_bal = models.DecimalField(max_digits=19, decimal_places=2)
    debt_adv = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.customer_name

class VendorDetails(models.Model):
    vendor_name = models.CharField(max_length=50, blank=False)
    vendor_address = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor_name

class Purchase(models.Model):
    receipt = models.CharField(max_length=50, null = True, blank = True)
    vendor = models.ForeignKey(VendorDetails, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(blank=True)
    amount_paid = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.receipt

class Sales(models.Model):
    receipt_no = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sales_date = models.DateTimeField(blank=True)
    customers_name = models.ForeignKey(CustomersDetails, on_delete=models.CASCADE)






