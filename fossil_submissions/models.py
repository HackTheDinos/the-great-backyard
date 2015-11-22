from django.db import models

def picture_upload_to(self, filename):
    return image_upload_to(self, re.sub(r'.*\.(\w+)', r'submission_img.\1', filename).lower())

class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image = models.ImageField(max_length=1000, upload_to=picture_upload_to, null=True, blank=True)
    approved = models.CharField(choices=(('Approved', 'Approved'), ('Uncertain', 'Uncertain'), ('Denied', 'Denied')))
    reviewed = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        ordering = ('created',)
