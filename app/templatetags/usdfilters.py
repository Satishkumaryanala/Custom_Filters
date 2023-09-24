from django import template

register = template.Library()

@register.filter(name='replace')
def replace(val,arg1):
    return val.replace(arg1,"Django")

@register.filter(name='swapcase')
def swap(val):
    return val.swapcase()

def Count(val,arg):
    return val.count(arg)


# 1st way of registration
""" register.filter('swapcase',swap)

register.filter('replace',replace) """

register.filter('Count',Count)
