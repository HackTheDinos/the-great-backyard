from fossil_submissions.models import Submission
from rest_framework.serializers import ModelSerializer

class SubmissionSerializer(ModelSerializer):
	class Meta:
		model = Submission
		fields = ('created', 'description', 'latitude', 'image', 'longitude', 'approved', 'reviewed')
		# read_only_fields = ('image',)