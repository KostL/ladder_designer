"""
Definition of urls for ladder_designer.
"""

from django.conf.urls import include, url
import ladder_designer_app.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', ladder_designer_app.views.index, name='index')
    # url(r'^ladder_designer/', include('ladder_designer.ladder_designer.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
