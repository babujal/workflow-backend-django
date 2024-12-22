from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WorkOrder(models.Model):
    unit_no = models.CharField(max_length=255, unique=True)
    customer = models.CharField(max_length=255)
    bay_no = models.CharField(
        max_length=5,
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('Yard', 'Yard'),
        ],
        default='Yard'
    )
    wo_status = models.CharField(
        max_length=15,
        choices=[
            ('WOAPPR', 'WOAPPR'),
            ('Approved', 'Approved'),
            ('Inspection', 'Inspection'),
            ('In Progress', 'In Progress'),
            ('Parts ordered', 'Parts ordered'),
            ('Declined', 'Declined'),
            ('Completed', 'Completed'),
            ('Pending', 'Pending'),
        ],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="WorkOrder")