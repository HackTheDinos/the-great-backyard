from rest_framework import viewsets
from fossil_submissions.models import Submission
from fossil_submissions.serializer import SubmissionSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
	queryset = Submission.objects.all()
	serializer_class = SubmissionSerializer