from django.db import models
from django.conf import settings

# Create your models here.
class Transactions(models.Model):
    # transaction id : valid trasaction id from mpesa
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    # phone number : valid phone number from mpesa that attempted to pay
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Mpesa receipt number
    mpesa_receipt_number = models.CharField(max_length=100, blank=True, null=True)

    # Status of transaction
    status = models.CharField(max_length=50, blank=True, null=True)

    # Description of transaction
    description = models.CharField(blank=True, null=True)

    #  Date of transaction
    transaction_date = models.DateField(
        auto_now_add=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Transaction = {self.mpesa_receipt_number}"
