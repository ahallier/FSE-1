from django.conf.urls import patterns, include, url
from django.contrib import admin, auth

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hospital.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^myLogin/', include('myLogin.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('myLogin.urls')),
    url(r'^/', include('myLogin.urls')),
)

