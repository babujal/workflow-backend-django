from django.db import models

# Create your models here.
class WorkOrder(models.Model):
    unit_no = models.CharField(max_length=255, unique=True)  # Translating String with unique constraint
    customer = models.CharField(max_length=255)  # Translating String with required=True
    bay_no = models.CharField(
        max_length=5,
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('Yard', 'Yard'),
        ],
        default='Yard'
    )  # Translating enum with default
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
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamps: created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamps: updated

    def __str__(self):
        return f"WorkOrder {self.unit_no} - {self.customer}"