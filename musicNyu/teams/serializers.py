from rest_framework import serializers
from bookings.models import TeamMembers
from Auth.models import User


class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ('name', 'role')