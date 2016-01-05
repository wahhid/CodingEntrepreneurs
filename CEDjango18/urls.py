from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]
