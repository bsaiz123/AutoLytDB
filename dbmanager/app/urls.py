from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^import/$', import_seq, name='import_seq'),
    url(r'^domains/$', domains, name='domains'),
    url(r'^sequences/$', sequences, name='sequences'),
    url(r'^details/(?P<accession_num>\w{0,50})/$', seq_details, name='seq_details'),
]