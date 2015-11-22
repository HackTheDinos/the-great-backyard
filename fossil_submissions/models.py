from django.db import models

def picture_upload_to(self, filename):
    return image_upload_to(self, re.sub(r'.*\.(\w+)', r'submission_img.\1', filename).lower())

class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image = models.ImageField(max_length=1000, upload_to=picture_upload_to, null=True, blank=True)
    approved = models.CharField(max_length=100, choices=(('Approved', 'Approved'), ('Uncertain', 'Uncertain'), ('Denied', 'Denied')), null=True, blank=True)
    reviewed = models.BooleanField(default=False)

    def __unicode__(self):
        return "Fossil Submission - {0}".format(self.id)

    class Meta:
        ordering = ('created',)
