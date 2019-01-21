from django import template

register = template.Library()

from ..models import Computer
from ..models import Laptop
from ..models import NetworkSwitch
from ..models import Printer
from ..models import AdditionalItem

@register.simple_tag
def equipment1_name():
    return Computer.__name__

@register.simple_tag
def equipment2_name():
    return Laptop.__name__

@register.simple_tag
def equipment3_name():
    return NetworkSwitch.__name__

@register.simple_tag
def equipment4_name():
    return Printer.__name__

@register.simple_tag
def equipment5_name():
    return AdditionalItem.__name__
