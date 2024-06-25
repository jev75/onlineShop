from django import template

register = template.Library()

@register.filter
def get_total_cart_price(cart_items):
    total = sum(item.product.price * item.quantity for item in cart_items)
    return f"{total:.2f}"

@register.filter
def multiply(value, arg):
    return value * arg
