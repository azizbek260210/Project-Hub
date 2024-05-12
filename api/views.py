from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from . import serializers
from main import models


@api_view(['GET'])
def index(request):
    """Banner ma'lumotlari"""
    data = models.Banner.objects.filter().order_by('-id')[0]
    serializer_data = serializers.BannerSerializer(data)
    return Response(serializer_data.data)


class PortfolioList(generics.ListAPIView):
    """Portfolio ma'lumotlari"""
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
    


class TeamsList(generics.ListAPIView):
    """Jamoa haqida ma'lumot"""
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


@api_view(['post'])
def create_message(request):
    name = request.data.get('name')
    phone = request.data.get('phone')
    content = request.data.get('content')
    if name and phone and content:
        models.Message.objects.create(
            name=name, 
            phone=phone, 
            content=content
            )
        return Response('Xabar muvaffaqqiyatli jo`natildi', status=status.HTTP_201_CREATED)
    return Response('Xatolik', status=status.HTTP_400_BAD_REQUEST)


class VacancyList(generics.ListAPIView):
    """Ish uchun o'rinlar"""
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancyListSerializer


class VacancyDetail(generics.RetrieveAPIView):
    """Ish o'rin haqida batafsil"""
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancyDetailSerializer


@api_view(['post'])
def create_vacancy_resume(request):
    full_name = request.data.get('full_name')
    cv = request.data.get('cv')
    phone = request.data.get('phone')
    if full_name and phone and cv:
        models.Resume.objects.create(
            full_name=full_name, 
            phone=phone, 
            cv=cv)
        return Response('Resume tayyor', status=status.HTTP_201_CREATED)
    return Response('Xatolik', status=status.HTTP_400_BAD_REQUEST)
