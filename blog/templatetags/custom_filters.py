# custom_filters.py
from collections import Counter as cntr
from django import template

register = template.Library()

@register.filter
def Marking(value):
    """Split a string into a list of paragraphs."""
    count = cntr(value[:3])
    if count["#"]: return count["#"]
    if count["-"]: return 10+count["-"]


@register.filter
def first_nchars(value,n):
    return value[:n]

@register.filter
def last_nchars(value,n):
    return value[n:]