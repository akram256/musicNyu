from django.db import models
from Auth.models import User
from helpers.models import BaseAbstractModel
from decimal import Decimal

# Create your models here.

# class GalleryCategory(BaseAbstractModel):
#     name=models.CharField(max_length=255, blank=True, null=True)

class TeamMembers(BaseAbstractModel):
    """models for gallery"""
    name=models.CharField(max_length=255, blank=True, null=True)
    role=models.CharField(max_length=255, blank=True, null=True)