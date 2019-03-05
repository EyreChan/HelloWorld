from django.conf.urls import url
from django.contrib import admin
from . import view, search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', view.hello),
    url(r'^print$', view.receive_data),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
]