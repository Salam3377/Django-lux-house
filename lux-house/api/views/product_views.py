from django.shortcuts import render, get_object_or_404
from ..models.product import Product
from  rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import ProductSerializer, ProductReadSerializer
from rest_framework import viewsets



class ProductView(APIView):
    authentication_classes = []
    permission_classes = []
    product = Product.objects.all()
    serializer_class = ProductSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)













# class ProductView(APIView):
#     authentication_classes = []
#     permission_classes = []
#     def get(self, request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many =True)
#         return Response({'menu': serializer.data})
    

# class ProductDetailView(APIView):
#     authentication_classes = []
#     permission_classes = []
#     """View class for menu/:pk for viewing sinlge menu, updating or removing single menu"""
#     serializer_class = ProductSerializer
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk) # first pk name second pk parameter
#         serializer = ProductReadSerializer(product)
#         return Response({'menus': serializer.data})
