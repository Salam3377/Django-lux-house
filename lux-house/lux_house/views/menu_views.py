from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from ..serializers import MenuSerializer
from ..models.menu import Menu


class MenuView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many =True)
        return Response({'authors': serializer.data})