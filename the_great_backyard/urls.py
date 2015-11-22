from fossil_submissions import views
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
# from django.contrib import admin

router = DefaultRouter()
router.register(r'submissions', views.SubmissionViewSet)


urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]
