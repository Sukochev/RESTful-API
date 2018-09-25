from rest_framework import serializers
from hints1.models import Hints


class HintsSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Hints
        fields = [
            'url',
            'pk', 
            'text', 
            'author', 
            'timestamp_pretty'
            ]

        read_only_fields = ['timestamp_pretty', 'pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


# Creted serializer for the HTML view. Just wanted to show the text information.
class HTMLSerializer(serializers.ModelSerializer):

    many=True

    class Meta:
        model = Hints
        fields = [ 
            'text', 
            ]

        read_only_fields = ['text',]

#Converts to JSON
#Validates data

