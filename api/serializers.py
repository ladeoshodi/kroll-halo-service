from rest_framework import serializers
from .models import KrollHaloMapping


class KrollHaloMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrollHaloMapping
        fields = "__all__"
