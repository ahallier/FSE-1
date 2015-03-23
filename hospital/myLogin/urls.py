from django.conf.urls import patterns, url

from myLogin import views
from django.conf import settings
#from django.contrib import auth

urlpatterns = patterns('', url(r'^yes/$', views.login_success, name = 'yes'),
			   url(r'^no/$',  views.login_fail, name = 'no'),
			   url(r'^loginTime/$', views.loginTime, name = 'index'),
 #		   url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
 			   url(r'^login_page/$', views.login_page, name = 'lpage'),
     			   url(r'^profile/$', views.login_after, name = 'afterr'),
)

