from rest_framework import viewsets
from rest_framework import filters
from django.contrib.auth.models import User
from fossil_submissions.models import Submission, Appraisal
from fossil_submissions.serializer import SubmissionSerializer, UserSerializer, AppraisalSerializer
from rest_framework import parsers
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from django.shortcuts import redirect, get_object_or_404

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('approved', 'reviewed',)
    search_fields = ('description',)
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        submissions = self.queryset
        response = super(SubmissionViewSet, self).list(request, *args, **kwargs)
        serializer = self.get_serializer()
        if request.accepted_renderer.format == 'html':
        	return Response({'submissions': submissions, 'serializer': serializer, 'type': type(response)}, template_name='submissions/list.html')
        return response

    def create(self, request, *args, **kwargs):
    	response = super(SubmissionViewSet, self).create(request, *args, **kwargs)
        serializer = SubmissionSerializer(data=response.data)
        if not serializer.is_valid():
        	return Response({'submission': serializer.errors, 'serializer': serializer}, template_name='submissions/list.html')
        return redirect('/submissions')

    def retrieve(self, request, pk, *args, **kwargs):
        submission = get_object_or_404(Submission, pk=pk)
        response = super(SubmissionViewSet, self).retrieve(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
        	return Response({'submission': submission}, template_name='submissions/retrieve.html')
        return response

    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AppraisalViewSet(viewsets.ModelViewSet):
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        appraisals = self.queryset
        response = super(AppraisalViewSet, self).list(request, *args, **kwargs)
        serializer = self.get_serializer()
        if request.accepted_renderer.format == 'html':
        	return Response({'appraisals': appraisals, 'serializer': serializer}, template_name='appraisals/list.html')
        return response

    def create(self, request, *args, **kwargs):
    	response = super(AppraisalViewSet, self).create(request, *args, **kwargs)
        serializer = AppraisalSerializer(data=response.data)
        if not serializer.is_valid():
        	return Response({'appraisals': serializer.errors, 'serializer': serializer}, template_name='appraisals/list.html')
        return redirect('/appraisals')

    def retrieve(self, request, pk, *args, **kwargs):
        appraisal = get_object_or_404(Appraisal, pk=pk)
        response = super(AppraisalViewSet, self).retrieve(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
        	return Response({'appraisal': appraisal}, template_name='appraisals/retrieve.html')
        return response

    def perform_create(self, serializer):
        serializer.save(appraiser=self.request.user)

