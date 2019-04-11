from django import template

register = template.Library()

from ..models import Item


# @register.simple_tag
# def equipment1_name():
#     return equipment[0].__name__
#
# @register.simple_tag
# def equipment2_name():
#     return equipment[1].__name__
#
# @register.simple_tag
# def equipment3_name():
#     return equipment[2].__name__
#
# @register.simple_tag
# def equipment4_name():
#     return equipment[3].__name__
#
# @register.simple_tag
# def equipment5_name():
#     return equipment[4].__name__


@register.simple_tag
def total_products_count():
    count = 0
    item = Item.objects.all()
    for obj in item:
        count += obj.working + obj.in_maintenance + obj.out_of_order

    return count


@register.simple_tag
def out_of_order_count():
    count = 0
    item = Item.objects.all()
    for obj in item:
        count += obj.out_of_order

    return count


@register.simple_tag
def in_maintenance_count():
    count = 0
    item = Item.objects.all()
    for obj in item:
        count += obj.in_maintenance

    return count