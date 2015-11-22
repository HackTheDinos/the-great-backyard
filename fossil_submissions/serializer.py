from django.contrib.auth.models import User
from fossil_submissions.models import Submission, Appraisal
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = ('created', 'description', 'latitude', 'image', 'longitude', 'approved', 'reviewed')

class UserSerializer(ModelSerializer):
    user_appraisals = PrimaryKeyRelatedField(many=True, queryset=Appraisal.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'user_appraisals',)

class AppraisalSerializer(ModelSerializer):
    appraiser = ReadOnlyField(source='appraiser.username')
    class Meta:
        model = Appraisal
        fields = ('appraiser', 'comment', 'submission', 'is_fossil')