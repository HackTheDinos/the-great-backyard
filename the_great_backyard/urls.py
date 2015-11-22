from fossil_submissions import views
from django.conf.urls import include, url
from django.conf import settings
from rest_framework.routers import DefaultRouter
# from django.contrib import admin

router = DefaultRouter()
router.register(r'submissions', views.SubmissionViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, })
]
