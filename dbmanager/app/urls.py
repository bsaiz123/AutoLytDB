from django.conf.urls import url

from .views import home, import_seq

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^import/$', import_seq, name='import_seq'),
]