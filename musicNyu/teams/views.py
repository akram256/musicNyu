from django.shortcuts import get_object_or_404
from rest_framework.generics import (UpdateAPIView,
                                     RetrieveUpdateAPIView,
                                     ListAPIView)
from teams.models import TeamMembers
from Auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TeamMembersSerializer
from rest_framework import status


class TeamMembersView(ListAPIView):
    serializer_class=TeamMembersSerializer
    permission_classes=(IsAuthenticated,)
    queryset=TeamMembers.objects.all()


    def post(self, request):
        post_data = {"name":request.data["name"],"role":request.data["role"]}
        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Team member has been added"},
                        status=status.HTTP_201_CREATED)

class TeamMembersRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    serializer_class=TeamMembersSerializer
    permission_classes=(IsAuthenticated,)
    queryset=TeamMembers.objects.all()
    lookup_field = 'id'
   

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(), id=self.kwargs.get('id'))

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message":'Successfully updated'},serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Team member has been successfully deleted"},
                        status=status.HTTP_204_NO_CONTENT)
