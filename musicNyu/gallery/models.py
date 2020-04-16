from django.db import models
from Auth.models import User
from helpers.models import BaseAbstractModel
from decimal import Decimal

# Create your models here.

# class GalleryCategory(BaseAbstractModel):
#     name=models.CharField(max_length=255, blank=True, null=True)

class Gallery(BaseAbstractModel):
    """models for gallery"""
    name=models.CharField(max_length=255, blank=True, null=True)
    image=models.models.ImageField(upload_to='gallery', null=True)
    description=models.CharField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True, null=True)
