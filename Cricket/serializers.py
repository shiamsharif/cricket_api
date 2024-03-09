from rest_framework import serializers

from Cricket.models import Cricket

class CricketSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Cricket
        fields ="__all__"