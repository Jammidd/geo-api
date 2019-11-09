from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet, generics
from rest_framework.response import Response

from countries.models import Country
from countries.serializers import CountrySerializer


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


class CountriesByContinentViewSet(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        continent_pk = self.kwargs['']