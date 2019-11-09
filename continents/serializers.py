from rest_framework.serializers import ModelSerializer

from continents.models import Continent


class ContinentSerializer(ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'