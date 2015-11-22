from rest_framework import viewsets
from rest_framework import filters
from django.contrib.auth.models import User
from fossil_submissions.models import Submission, Appraisal
from fossil_submissions.serializer import SubmissionSerializer, UserSerializer, AppraisalSerializer
from rest_framework import parsers

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('approved', 'reviewed',)
    search_fields = ('description',)

    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AppraisalViewSet(viewsets.ModelViewSet):
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer