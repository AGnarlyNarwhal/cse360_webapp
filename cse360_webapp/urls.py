from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf.urls.static import static
from app1 import views

#This is the project/url.py 
 
urlpatterns = patterns('',
    # Examples:
    url(r'^home/', 'app1.views.events'),
    url(r'^app1/', include('app1.urls')),
    url(r'^accounts/', include('userprofile.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #Gives out our media root to serve pictures   
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT }),
    #Gives out the static root to serve static files (images,css,js, etc.)    
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #{'document_root': settings.STATIC_ROOT }),

    #User login/authentication/registration urls
    #url(r'^accounts/user_image_upload/$', 'cse360_webapp.views.user_image_upload'
    url(r'^accounts/tickets/$', 'app1.views.tickets'),
    url(r'^accounts/login/$', 'cse360_webapp.views.login'),
    url(r'^accounts/auth/$', 'cse360_webapp.views.auth_view'),
    url(r'^accounts/logout/$', 'cse360_webapp.views.logout'),
    url(r'^accounts/loggedin/$', 'cse360_webapp.views.loggedin'),
    url(r'^accounts/invalid/$', 'cse360_webapp.views.invalid_login'),
    url(r'^accounts/register/$', 'cse360_webapp.views.register_user'),
    url(r'^accounts/register_success/$',
        'cse360_webapp.views.register_success'),
    
)
"""
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
"""	
if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
