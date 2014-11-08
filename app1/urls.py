from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static 
from app1 import views

#this is the project/app url.py 

urlpatterns = patterns('',
    url(r'^all/$','app1.views.events' ),
    url(r'^get/(?P<event_id>\d+)/$', 'app1.views.event'),
    #url(r'^event/publish/$', 'app1.views.publish'),
    url(r'^event/buy/(?P<event_id>\d+)/(?P<num_ticks>\d+)/$', 'app1.views.buytickets'),    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
    
   
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


