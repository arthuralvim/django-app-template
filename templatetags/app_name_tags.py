# -*- coding: utf-8 -*-

from django import template
register = template.Library()

@register.filter
def is_not_none(arg):
    """
    Check if an attribute is None.
    """
    return arg is not None


@register.filter
def get_range(value):
    """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>
    {% templatetag openblock %} for i in 3|get_range {% templatetag closeblock %}
      <li> {% templatetag openvariable %} i {% templatetag closevariable %} . Do something</li>
    {% templatetag openblock %} endfor {% templatetag closeblock %}
    </ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
    """
    return range(0, int(value)+1)
