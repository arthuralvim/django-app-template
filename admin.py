# -*- coding: utf-8 -*-

from django.contrib import admin
from {{ app_name }}.models import {{ app_name|title }}


class {{ app_name|title }}Admin(admin.ModelAdmin):
    date_hierarchy = 'example_datetimefield'
    list_display = ('example_charfield', 'example_textfield',
                    'example_datetimefield', )
    list_display_links = ['example_charfield', ]
    list_filter = ['example_booleanfield', ]
    prepopulated_fields = {'slug': ('example_charfield',)}
    search_fields = ['example_charfield', 'example_textfield', ]
    ordering = ('example_charfield',)

admin.site.register({{ app_name|title }}, {{ app_name|title }}Admin)
