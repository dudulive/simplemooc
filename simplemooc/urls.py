from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = ['',
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
]
