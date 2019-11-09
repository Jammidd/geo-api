from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from continents.models import Continent
from continents.serializers import ContinentSerializer

from countries.models import Country
from countries.serializers import CountrySerializer


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

    @action(methods=['get'], detail=False, url_path='(?P<pk>[a-zA-Z0-9]+)/countries/?')
    def countries(self, request, pk=None):
        countries = Country.objects.all()
        if pk and pk.isnumeric():
            countries = countries.filter(continent__pk=pk)
        elif pk:
            countries = countries.filter(continent__code__iexact=pk)

        countries.order_by('name')

        page = self.paginate_queryset(countries)
        if page is not None:
            serializer = CountrySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)