# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify


class {{ app_name|title }}(models.Model):

    # example_field = models.Field
    #     blank: If True, the field is allowed to be blank. Default is False.
    #     choices: An iterable (e.g., a list or tuple) to use as choices for this field.
    #     db_column: The name of the database column to use for this field.
    #     db_index: If True, django-admin.py sqlindexes will output a CREATE INDEX statement for this field.
    #     default: The default value for the field.
    #     editable: If False, the field will not be displayed in the admin or any other ModelForm. Default is True.
    #     error_messages: The error_messages argument lets you override the default messages that the field will raise.
    #     help_text: Extra “help” text to be displayed with the form widget.
    #     primary_key: If True, this field is the primary key for the model.
    #     null: If True, Django will store empty values as NULL in the database. Default is False.
    #     unique: If True, this field must be unique throughout the table.
    #     validators: A list of validators to run for this field. See the validators documentation for more information.
    #     verbose_name: A human-readable name for the field. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces. See Verbose field names.

    example_binaryfield = models.BinaryField(
        verbose_name=_(u'example_binaryfield'),
        blank=False,
        null=False, )
    example_charfield = models.CharField(
        verbose_name=_(u'example_charfield'),
        max_length=255,
        blank=False,
        null=False, )
    example_commaseparatedintegerfield = models.CommaSeparatedIntegerField(
        verbose_name=_(u'example_commaseparatedintegerfield'),
        max_length=255,
        blank=False,
        null=False, )
    example_emailfield = models.EmailField(
        verbose_name=_(u'example_emailfield'),
        max_length=254,
        blank=False,
        null=False, )
    example_textfield = models.TextField(
        verbose_name=_(u'example_textfield'),
        blank=False,
        null=False, )
    example_slugfield = models.SlugField(
        verbose_name=_(u'example_slugfield'),
        max_length=255,
        default='',
        blank=True,
        null=True, )
    example_booleanfield = models.BooleanField(
        verbose_name=_(u'example_booleanfield'),
        default=False,
        blank=True, )
    example_nullbooleanfield = models.NullBooleanField(
        verbose_name=_(u'example_nullbooleanfield'),
        default=False,
        blank=True,
        null=True, )
    example_datefield = models.DateField(
        verbose_name=_(u'example_datefield'),
        auto_now_add=True,
        auto_now=True,
        blank=True,
        null=True, )
    example_datetimefield = models.DateTimeField(
        auto_now_add=True,
        auto_now=True,
        blank=True,
        null=True, )
    example_timefield = models.TimeField(
        auto_now_add=True,
        auto_now=True,
        blank=True,
        null=True, )
    example_urlfield = models.URLField(
        verbose_name=_(u'example_urlfield'),
        blank=True,
        null=True, )
    example_integerfield = models.IntegerField(
        verbose_name=_(u'example_integerfield'),
        default=0,
        blank=True,
        null=True, )
    example_pintegerfield = models.PositiveIntegerField(
        verbose_name=_(u'example_pintegerfield'),
        default=0,
        blank=True,
        null=True, )
    example_floatfield = models.FloatField(
        verbose_name=_(u'example_floatfield'),
        default=0,
        blank=True,
        null=True, )
    example_ipaddressfield = models.IPAddressField(
        verbose_name=_(u'example_ipaddressfield'),
        blank=True,
        null=True, )
    example_decimalfield = models.DecimalField(
        verbose_name=_(u'example_decimalfield'),
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True,
        null=True, )
    example_filefield = models.FileField(
        verbose_name=_(u'example_filefield'),
        upload_to='files-upload-path',
        blank=True,
        null=True, )
    example_imagefield = models.FileField(
        verbose_name=_(u'example_imagefield'),
        upload_to='images-upload-path',
        blank=True,
        null=True, )

    def __unicode__(self):
        return self.example_charfield

    def get_absolute_url(self):
        return reverse_lazy('{{ app_name }}:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.example_slugfield:
            self.example_slugfield = slugify(self.example_charfield)
        super({{ app_name|title }}, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'{{ app_name }}')
        verbose_name_plural = _(u'{{ app_name }}s')
