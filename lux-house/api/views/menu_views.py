from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from ..serializers import MenuSerializer, MenuReadSerializer
from ..models.menu import Menu

class MenuView(APIView):
    authentication_classes = []
    permission_classes = []
  
    def get(self, request):
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many =True)
        return Response({'menu': serializer.data})
        
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = self.queryset.filter(owner=user)
    #     return queryset

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

# class MenuView(APIView):
#     authentication_classes = []
#     permission_classes = []
#     def get(self, request):
#         menu = Menu.objects.all()
#         serializer = MenuSerializer(menu, many =True)
#         return Response({'menu': serializer.data})
    
#     def post(self,request):
#         serializer = MenuSerializer(data=request.data)# left data name, takes request data in
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetailView(APIView):
    authentication_classes = []
    permission_classes = []
    """View class for menu/:pk for viewing sinlge menu, updating or removing single menu"""
    serializer_class = MenuSerializer
    def get(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk) # first pk name second pk parameter
        serializer = MenuReadSerializer(menu)
        return Response({'menus': serializer.data})

    def patch(self, request, pk):  #update
        menu = get_object_or_404(Menu, pk=pk) # first pk name second pk parameter
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        