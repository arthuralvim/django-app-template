# -*- coding: utf-8 -*-
from {{ app_name }}.models import {{ app_name|title }}
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class {{ app_name|title }}DetailView(DetailView):
    model = {{ app_name|title }}

class {{ app_name|title }}CreateView(CreateView):
    model = {{ app_name|title }}

class {{ app_name|title }}UpdateView(UpdateView):
    model = {{ app_name|title }}

class {{ app_name|title }}DeleteView(DeleteView):
    model = {{ app_name|title }}
    success_url = reverse_lazy('{{ app_name }}:list')

class {{ app_name|title }}ListView(ListView):
    model = {{ app_name|title }}

{{ app_name }}_list = {{ app_name|title }}ListView.as_view()
{{ app_name }}_detail = {{ app_name|title }}DetailView.as_view()
{{ app_name }}_delete = {{ app_name|title }}DeleteView.as_view()
{{ app_name }}_update = {{ app_name|title }}UpdateView.as_view()
{{ app_name }}_create = {{ app_name|title }}CreateView.as_view()


# do some rest api with django rest framework.

# from rest_framework.generics import ListCreateAPIView
# from rest_framework.generics import RetrieveUpdateAPIView
# from {{ app_name }}.serializers import {{ app_name|title }}Serializer

# class {{ app_name|title }}APIListCreateView(ListCreateAPIView):
#     queryset = {{ app_name|title }}.objects.all()
#     serializer_class = {{ app_name|title }}Serializer


# class {{ app_name|title }}APIDetail(RetrieveUpdateAPIView):
#     queryset = {{ app_name|title }}.objects.all()
#     serializer_class = {{ app_name|title }}Serializer


# {{ app_name }}apilist = {{ app_name|title }}APIListCreateView.as_view()
# {{ app_name }}apidetail = {{ app_name|title }}APIDetail.as_view()
