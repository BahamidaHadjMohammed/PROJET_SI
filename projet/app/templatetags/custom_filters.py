# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='getattr')
def getattribute(value, arg):

     resu =value[arg]
     return resu
      
    
 