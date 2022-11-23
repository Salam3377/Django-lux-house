from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from ..serializers import MenuSerializer
from ..models.menu import Menu


class MenuView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many =True)
        return Response({'menu': serializer.data})