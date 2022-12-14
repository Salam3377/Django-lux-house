from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from ..serializers import CartSerializer, CartReadSerializer
from ..models.cart import Cart
from ..models.menu import Product
from ..models.user import User
from ..serializers import ProductSerializer


class CartView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        print('GET: ', request)
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many =True)
        res = []
        print(serializer.data)
        for object in serializer.data:
            print(object['product'])
            p = get_object_or_404(Product, pk=object['product'])
            product_serializer = ProductSerializer(p)
            res.append(product_serializer.data)
        
        return Response({'cart': res})
    def post(self,request, pk):
        print('POST: ', request.data, ' | ', pk)
        p = get_object_or_404(Product, pk=pk)
        u = get_object_or_404(User, pk=1)
        serializer = CartSerializer(data={'product': p.id, 'owner': 1})# left data name, takes request data in
        if serializer.is_valid():
            # c = Cart.objects.create(Product=p, User=0)
            # c.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CartDetailView(APIView):
    authentication_classes = []
    permission_classes = []
    # """View class for menu/:pk for viewing sinlge menu, updating or removing single menu"""
    serializer_class = CartSerializer
    def get(self, request, pk):
        print('CART DETAIL VIEW - GET: ', request , ' | ', pk)
        # cart = get_object_or_404(CartProducts, pk=pk) # first pk name second pk parameter
        # serializer = CartReadSerializer(cart)
        # return Response({'cart': serializer.data})

    def post(self, request, pk):  #update
        print('CART DETAIL VIEW - POST: ', request , ' | ', pk)
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
        