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
    if count["$"]: return 20+count["$"]


@register.filter
def first_nchars(value,n):
    return value[:n]

@register.filter
def last_nchars(value,n):
    return value[n:]

@register.filter
def title_case(value):
    return value.title()


@register.filter(name='attr')
def attr(value, arg):
    attrs = {}
    for pair in arg.split(';'):
        try:
            key, value = pair.split(':')
            attrs[key] = value
        except ValueError:
            pass
    return value.as_widget(attrs=attrs)

@register.filter(name='add_class')
def add_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split()
    css_classes.append(arg)
    value.field.widget.attrs['class'] = ' '.join(css_classes)
    return value

@register.filter
def makelister(value):
    return value.split("\n")

@register.filter
def Maker(value):
    """Split a string into a list of paragraphs."""
    l = ""

    for v in value:
        if "#" in v:
            v = v.replace("#", "")
        if "-" in v:
            v = v.replace("-", "")
        if "$" in v:
            v = v.replace("$", "")
        l+= v

    return l

@register.filter
def catego(value):
    """Split a string into a list of paragraphs."""
    return [i["name"] for i in value.values()]

@register.filter
def catego_split(r):
    h = [[],[]]
    for j in range(2):
        for i in range(len(r)):
            if i%2==j:
                h[j].append(r[i])
    # for i in range(len(r)):
    #     if i%2==1:
    #         h[1].append(r[i])
    
    if len(h[0]) > len(h[1]):
        h[1].append(None)
    else:
        h[0].append(None)
    return h