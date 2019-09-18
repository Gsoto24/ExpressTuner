from django.db import models

# Create your models here.
class CSVRecord(models.Model):
    # Email, CustomerID, ProductID, Price, TimestampCreated, Attempts
    email = models.CharField(default=None, null=True, blank=True, max_length=500)
    customer_id = models.CharField(default=None, null=True, blank=True, max_length=500)
    product_id = models.CharField(default=None, null=True, blank=True, max_length=500)
    price = models.CharField(default=None, null=True, blank=True, max_length=500)
    attempts = models.IntegerField(default = 0,null=True, blank=True)
    status = (
        (0, 'Charged'),
        (1, 'Attempting'),
        (2, 'Failed'),
    )
    status_code = models.IntegerField(
        choices=status,
    )
    status_text = models.TextField(default=None, null=True, blank=True)
    scheduled_date = models.DateField(default=None, null=True, blank=True)
    firstattempt = models.DateField(default=None, null=True, blank=True)
    secondattempt = models.DateField(default=None, null=True, blank=True)
    expiration = models.DateField(default=None, null=True, blank=True)
    action_date = models.DateField(default=None, null=True, blank=True)
    last_modified_by =  models.CharField(default=None, null=True, blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
