from django.shortcuts import get_object_or_404
from rest_framework.generics import (UpdateAPIView,
                                     RetrieveUpdateAPIView,
                                     ListAPIView)
from gallery.models import Gallery
from Auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import GallerySerializer
from rest_framework import status


class GalleryView(ListAPIView):
    serializer_class=GallerySerializer
    permission_classes=(IsAuthenticated,)
    queryset=Gallery.objects.all()


    def post(self, request):
        post_data = {"name":request.data["name"],"description":request.data["description"],"image":request.data["image"],"location":request.data["location"]}
        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"image has been created"},
                        status=status.HTTP_201_CREATED)

class GalleryrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    serializer_class=GallerySerializer
    permission_classes=(IsAuthenticated,)
    queryset=Gallery.objects.all()
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
        return Response({"message": "Image has been successfully deleted"},
                        status=status.HTTP_204_NO_CONTENT)
