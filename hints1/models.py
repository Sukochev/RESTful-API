from django.db import models
from rest_framework.reverse import reverse as api_reverse

# Create your models here.


class Hints(models.Model):

    text = models.TextField(max_length=255)
    author = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return str(self.text)

    def timestamp_pretty(self):
        return self.timestamp.strftime('%b %d %Y')

# This creates a url that I use in Serializers as a link to the individual HintsRudView
    def get_api_url(self, request=None):
        return api_reverse("api-hints1:hints-rud", kwargs={'pk': self.pk}, request=request)