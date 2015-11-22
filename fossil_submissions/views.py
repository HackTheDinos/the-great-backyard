from rest_framework import viewsets
from rest_framework import filters
from fossil_submissions.models import Submission
from fossil_submissions.serializer import SubmissionSerializer
from rest_framework import parsers

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('approved', 'reviewed',)

    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))