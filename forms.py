# -*- coding: utf-8 -*-

from django import forms
from {{ app_name }}.models import {{ app_name|title }}


class {{ app_name|title }}Form(forms.ModelForm):
    class Meta:
        model = {{ app_name|title }}
