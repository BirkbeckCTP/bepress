__copyright__ = "Copyright 2017 Birkbeck, University of London"
__author__ = "Martin Paul Eve & Andy Byers"
__license__ = "AGPL v3"
__maintainer__ = "Birkbeck Centre for Technology and Publishing"

from django.conf.urls import url

from plugins.bepress import views

urlpatterns = [
    url(r'^$', views.index, name='bepress_index'),
    url(r'^index/$', views.index, name='bepress_index'),
    url(r'^import/$', views.import_bepress_articles, name='bepress_import'),
    url(r'^csv_import/$', views.import_bepress_csv, name='bepress_csv_import'),
]
