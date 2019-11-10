from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet, generics
from rest_framework.response import Response

from regions.models import Region
from regions.serializers import RegionSerializer


# Create your views here.
class RegionViewSet(ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    permission_classes = []
    serializer_class = RegionSerializer
