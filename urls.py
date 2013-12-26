# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('',
    url(r'^$', '{{ app_name }}.views.generic_list', name='list'),
    url(r'^add/$', '{{ app_name }}.views.generic_create', name='create'),
    url(r'^(?P<pk>\d+)/$', '{{ app_name }}.views.generic_detail', name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', '{{ app_name }}.views.generic_delete', name='delete'),
    url(r'^(?P<pk>\d+)/edit/$', '{{ app_name }}.views.generic_update', name='update'),

    # serializers
    url(r'^api/{{ app_name }}/$', '{{ app_name }}.serializers.{{ app_name }}apilist' , name='api-list', ),
    url(r'^api/{{ app_name }}/(?P<pk>\d+)/$', '{{ app_name }}.serializers.{{ app_name }}apidetail', name='api-detail', ),
)


