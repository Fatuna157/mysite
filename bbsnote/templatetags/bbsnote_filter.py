from django import template

register = template.Library()

#빼기 도구를 만들어서 사용함
@register.filter
def sub(value, arg):
    return value - arg