from rest_framework.viewsets import ModelViewSet

from Cricket.models import Cricket
from Cricket.serializers import CricketSerilizer


class CricketViewSet(ModelViewSet):
    serializer_class = CricketSerilizer
    queryset = Cricket.objects.all()
