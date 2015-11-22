from django.contrib.auth.models import User
from fossil_submissions.models import Submission, Appraisal
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ReadOnlyField, HyperlinkedRelatedField

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id', 'created', 'description', 'latitude', 'image', 'longitude', 'approved', 'reviewed')

class UserSerializer(ModelSerializer):
    user_appraisals = HyperlinkedRelatedField(view_name='appraisal-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'user_appraisals', 'password',)
        read_only_fields = ('user_appraisals',)

    def create(self, validated_data):
        user_data = {key: value for key, value in validated_data.items() if key != 'user_appraisals'}
        user = User.objects.create_user(**user_data)
        return user

class AppraisalSerializer(ModelSerializer):
    appraiser = ReadOnlyField(source='appraiser.username')
    submission = HyperlinkedRelatedField(queryset=Submission.objects.all(), view_name='submission-detail')
    class Meta:
        model = Appraisal
        fields = ('appraiser', 'comment', 'submission', 'is_fossil')