from loadtest.views import LoadTestView
from django.conf.urls import patterns, url

urlpatterns = patterns(
    url(r'^$', LoadTestView.as_view()),
    url(r'^loadtest/$', LoadTestView.as_view(), name='loadtest')
)
