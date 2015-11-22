from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

def image_upload_to(instance, filename):
    model = instance.__class__.__name__.lower()
    review_status = 'reviewed' if instance.reviewed else 'needs_review'
    return 'images/{model}/{review_status}/{filename}'.format(model=model, review_status=review_status, filename=filename)

def picture_upload_to(self, filename):
    return image_upload_to(self, filename)

class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    image = models.ImageField(max_length=1000, upload_to=picture_upload_to, null=True, blank=True)
    approved = models.CharField(max_length=100, choices=(('Approved', 'Approved'), ('Uncertain', 'Uncertain'), ('Denied', 'Denied')), null=True, blank=True)
    reviewed = models.BooleanField(default=False)

    def __unicode__(self):
        return "Submission_{0}".format(self.id)

    class Meta:
        ordering = ('created',)

class Appraisal(models.Model):
    appraiser = models.ForeignKey('auth.User', related_name='user_appraisals')
    submission = models.ForeignKey('Submission', unique=True, related_name='submission_appraisals')
    is_fossil =  models.CharField(max_length=100, choices=(('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')), default='Maybe')
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{0}: {1} ({2})".format(self.submission, self.is_fossil, self.appraiser.username)


@receiver(post_save, sender=Appraisal)
def update_submission_approval_status(sender, instance, created, **kwargs):
    status_map = {'Maybe': 'Uncertain', 'Yes': 'Approved', 'No': 'Denied'}
    submission = instance.submission
    submission.approved = status_map[instance.is_fossil]
    submission.reviewed = True
    submission.save()