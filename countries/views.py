from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet, generics
from rest_framework.response import Response

from countries.models import Country
from countries.serializers import CountrySerializer

from regions.models import Region
from regions.serializers import RegionSerializer


# Create your views here.
class CountryViewSet(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    permission_classes = []
    serializer_class = CountrySerializer

    def retrieve(self, request, pk=None):
        queryset = Country.objects.all()

        if pk and len(pk) > 2:
            country = get_object_or_404(queryset, pk=pk)
        elif pk:
            country = get_object_or_404(queryset, alpha_2_code__iexact=pk)

        serializer = CountrySerializer(country)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='(?P<pk>[a-zA-Z0-9]+)/regions/?')
    def regions(self, request, pk=None):
        regions = Region.objects.all()
        if pk and pk.isnumeric():
            regions = regions.filter(country__pk=pk)
        elif pk:
            regions = regions.filter(country__alpha_2_code__iexact=pk)

        regions.order_by('name')

        page = self.paginate_queryset(regions)
        if page is not None:
            serializer = RegionSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)