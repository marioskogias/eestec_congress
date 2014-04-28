from django.conf.urls import patterns, include, url
from congress_presence.views import BaseView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'here/$', BaseView.as_view()),
    url(r'here/(?P<id>[0-9]+)/$', BaseView.as_view()),
    # url(r'^congress/', include('congress.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
