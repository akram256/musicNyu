from django.shortcuts import get_object_or_404
from rest_framework.generics import (UpdateAPIView,
                                     RetrieveUpdateAPIView,
                                     ListAPIView)
from blogs.models import Blogs
from Auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializer
from rest_framework import status


class BlogsView(ListAPIView):
    serializer_class=BlogSerializer
    permission_classes=(IsAuthenticated,)
    queryset=Blogs.objects.all()


    def post(self, request):
        post_data = {"title":request.data["title"],"blog":request.data["blog"]}
        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Blog has been created"},
                        status=status.HTTP_201_CREATED)

class BlogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    serializer_class=BlogSerializer
    permission_classes=(IsAuthenticated,)
    queryset=Blogs.objects.all()
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
        return Response({"message": "Blog has been successfully deleted"},
                        status=status.HTTP_204_NO_CONTENT)
