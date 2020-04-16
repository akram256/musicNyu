from django.db import models
from Auth.models import User
from helpers.models import BaseAbstractModel
from decimal import Decimal


class Courses(BaseAbstractModel):
    """models for courses"""
    name=models.CharField(max_length=255, blank=True, null=True)
    description=models.CharField(max_length=255, blank=True, null=True)
    price=models.DecimalField(max_digits=12, decimal_places=2, null=True, default=Decimal('0.00'))
