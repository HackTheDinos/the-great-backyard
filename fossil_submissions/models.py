from django.db import models
from django.contrib.gis.geos import Point

def picture_upload_to(self, filename):
    return image_upload_to(self, re.sub(r'.*\.(\w+)', r'submission_img.\1', filename).lower())

class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image = models.ImageField(max_length=1000, upload_to=picture_upload_to, null=True, blank=True)

    class Meta:
        ordering = ('created',)

    @property
    def location_as_point(self):
        if self.latitude and self.longitude:
            return Point(self.longitude, self.latitude)
        return None
