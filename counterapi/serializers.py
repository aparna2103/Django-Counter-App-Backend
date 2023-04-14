from rest_framework import serializers

from .models import Counter

class CounterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Counter
        fields = ('name', 'latitube', 'longitude', 'geography')