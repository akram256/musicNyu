from rest_framework import serializers
from gallery.models import Gallery
from Auth.models import User


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('name', 'description', 'image','location',)