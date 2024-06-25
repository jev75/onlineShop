from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from store.models import Size


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('paysera', 'Paysera sąskaita'),
        ('swedbank', 'AB "Swedbank" bankas'),
        ('seb', 'AB bankas "SEB"'),
        ('luminor', 'Luminor'),
        ('siauliu', 'AB "Šiaulių bankas"'),
        ('revolut', 'Revolut (LT)'),
        ('citadele', 'AS "Citadele bankas"'),
        ('urbo', 'UAB Urbo bankas'),
        ('lku', 'Lietuvos centrinė kredito unija'),
        ('n26', 'N26 Bank (LT)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Vartotojas')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atnaujinta')
    is_paid = models.BooleanField(default=False, verbose_name='Apmokėta')
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_CHOICES,
        verbose_name='Apmokėjimo būdas',
        default='paysera'
    )

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

    def __str__(self):
        return f"Užsakymas {self.id} by {self.user.username}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Užsakymas')
    product = models.CharField(max_length=255, verbose_name='Produktas')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Kiekis')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Kaina')

    class Meta:
        verbose_name = 'Užsakymo prekė'
        verbose_name_plural = 'Užsakymo prekės'

    def __str__(self):
        return f"{self.product} ({self.quantity})"

    def get_cost(self):
        return self.price * self.quantity

class CartItem(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="Produkto tipas")
    object_id = models.PositiveIntegerField(verbose_name="Produkto ID")
    product = GenericForeignKey('content_type', 'object_id')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Dydis")


    quantity = models.PositiveIntegerField(default=1, verbose_name="Kiekis")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Vartotojas")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Pridėjimo data")

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    class Meta:
        verbose_name = "Krepšelio prekė"
        verbose_name_plural = "Krepšelio prekės"




