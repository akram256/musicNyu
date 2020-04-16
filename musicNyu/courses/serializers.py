from rest_framework import serializers
from bookings.models import Courses
from Auth.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('name', 'description', 'price',)