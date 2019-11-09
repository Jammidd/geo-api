from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from continents.models import Continent
from continents.serializers import ContinentSerializer


# Create your views here.
class ContinentViewSet(ReadOnlyModelViewSet):
    queryset = Continent.objects.all()
    permission_classes = []
    serializer_class = ContinentSerializer

    def retrieve(self, request, pk=None):
        queryset = Continent.objects.all()

        if pk and pk.isnumeric():
            continent = get_object_or_404(queryset, pk=pk)
        elif pk:
            continent = get_object_or_404(queryset, code__iexact=pk)

        serializer = ContinentSerializer(continent)
        return Response(serializer.data)