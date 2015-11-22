from rest_framework import viewsets
from rest_framework import filters
from django.contrib.auth.models import User
from fossil_submissions.models import Submission, Appraisal
from fossil_submissions.serializer import SubmissionSerializer, UserSerializer, AppraisalSerializer
from rest_framework import parsers
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from django.shortcuts import redirect

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('approved', 'reviewed',)
    search_fields = ('description',)
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(SubmissionViewSet, self).list(request, *args, **kwargs)
        serializer = self.get_serializer()
        if request.accepted_renderer.format == 'html':
        	return Response({'submissions': response.data, 'serializer': serializer}, template_name='submissions/list.html')
        return response

    def create(self, request, *args, **kwargs):
    	response = super(SubmissionViewSet, self).create(request, *args, **kwargs)
        serializer = SubmissionSerializer(data=response.data)
        if not serializer.is_valid():
        	return Response({'data': serializer.errors, 'serializer': serializer}, template_name='submissions/list.html')
        return redirect('/submissions')

    def retrieve(self, request, *args, **kwargs):
        response = super(SubmissionViewSet, self).retrieve(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
        	return Response({'data': response.data}, template_name='submissions/retrieve.html')
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
        response = super(SubmissionViewSet, self).list(request, *args, **kwargs)
        serializer = self.get_serializer()
        if request.accepted_renderer.format == 'html':
        	return Response({'submissions': response.data, 'serializer': serializer}, template_name='submissions/list.html')
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super(AppraisalViewSet, self).retrieve(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
        	return Response({'data': response.data}, template_name='appraisals/retrieve.html')
        return response

    def perform_create(self, serializer):
        serializer.save(appraiser=self.request.user)

