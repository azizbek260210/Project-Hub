from rest_framework.serializers import ModelSerializer
from main import models


class BannerSerializer(ModelSerializer):
    class Meta:
        model = models.Banner
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'


class VacancyListSerializer(ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ['id', 'job_title', 'working_day', 'working_time', 'salary']


class VacancyDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = '__all__'
