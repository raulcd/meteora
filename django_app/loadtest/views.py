from urllib.parse import urlparse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.core.urlresolvers import reverse


class LoadTestView(TemplateView):
    template_name = 'loadtest.html'

    def get_context_data(self, **kwargs):
        context = super(LoadTestView, self).get_context_data(**kwargs)

        results = []
        root_urlconf = __import__(settings.ROOT_URLCONF)

        def parse_urls(urls, path=''):
            for entry in urls:
                results.append(path + entry.regex.pattern[1:])
                if hasattr(entry, 'url_patterns'):
                    parse_urls(entry.url_patterns, path=path + entry.regex.pattern[1:])

        parse_urls(root_urlconf.urls.urlpatterns)

        context['available_views'] = results
        return context
