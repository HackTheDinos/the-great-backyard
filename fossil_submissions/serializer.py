from django.contrib.auth.models import User
from fossil_submissions.models import Submission
from rest_framework.serializers import ModelSerializer

class SubmissionSerializer(ModelSerializer):
	class Meta:
		model = Submission
		fields = ('created', 'description', 'latitude', 'image', 'longitude', 'approved', 'reviewed')

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')