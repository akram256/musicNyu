from rest_framework import serializers
from bookings.models import Blogs
from Auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ('user', 'title', 'blog',)