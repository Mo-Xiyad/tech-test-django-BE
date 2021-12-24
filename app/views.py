from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import HotListModel, ProductModel
from .serializers import HotListModelSerializer,ProductModelSerializer
from rest_framework import status


class HotListView(ListAPIView):
    queryset = HotListModel.objects.order_by('-date_created')
    serializer_class = HotListModelSerializer
    permission_classes = (permissions.AllowAny, )

class HotListCategoryView(APIView):
    serializer_class = HotListModelSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = HotListModel.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = HotListModelSerializer(queryset, many=True)

        return Response(serializer.data)

class HotListFeaturedView(ListAPIView):
    queryset = HotListModel.objects.all().filter(featured=True)
    serializer_class = HotListModelSerializer
    permission_classes = (permissions.AllowAny, )


class ProductsItemViews(APIView):
    def get(self, request, id=None):
        if id:
            item = ProductModel.objects.get(id=id)
            serializer = ProductModelSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = ProductModel.objects.all()
        serializer = ProductModelSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        item = get_object_or_404(ProductModel, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})