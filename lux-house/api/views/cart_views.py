from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from ..serializers import CartSerializer, CartReadSerializer
from ..models.cart import Cart
from ..models.menu import Menu


class CartView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many =True)
        return Response({'cart': serializer.data})
    # def post(self,request):
    #     serializer = CartSerializer(data=request.data)# left data name, takes request data in
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CartDetailView(APIView):
    authentication_classes = []
    permission_classes = []
    """View class for menu/:pk for viewing sinlge menu, updating or removing single menu"""
    # serializer_class = CartSerializer
    # def get(self, request, pk):
    #     cart = get_object_or_404(CartProducts, pk=pk) # first pk name second pk parameter
    #     serializer = CartReadSerializer(cart)
    #     return Response({'cart': serializer.data})

    # def patch(self, request, pk):  #update
    #     cart = get_object_or_404(CartProducts, pk=pk) # first pk name second pk parameter
    #     serializer = CartSerializer(cart, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     cart = get_object_or_404(CartProducts, pk=pk)
    #     cart.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
        