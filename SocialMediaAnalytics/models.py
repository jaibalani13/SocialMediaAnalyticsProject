from django.db import models


class SocialMediaPost(models.Model):
    content = models.TextField()
    identifier = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.identifier

    class Meta:
        app_label = 'SocialMediaAnalytics'
