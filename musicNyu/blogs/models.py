from django.db import models
from Auth.models import User
from helpers.models import BaseAbstractModel
from decimal import Decimal
# Create your models here.
class Blogs(BaseAbstractModel):
user=models.ForeignKey(to='User', on_delete=models.CASCADE)
title=models.CharField(max_length=255, blank=True, null=True)
blog=models.TextField(null=True)