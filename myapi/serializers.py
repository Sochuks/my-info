from rest_framework import serializers
from .models import Details


class DetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ('slackUsername', 'backend', 'age', 'bio')


