from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Pavadinimas', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategorija'
        verbose_name_plural = 'Kategorijos'

class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Pavadinimas', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategorija')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subkategorija'
        verbose_name_plural = 'Subkategorijos'

class Size(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Tipas')
    size = models.CharField(max_length=10, verbose_name='Dydis')

    def __str__(self):
        return f"{self.size} ({self.category})"

    class Meta:
        verbose_name = 'Dydis'
        verbose_name_plural = 'Dydžiai'
        ordering = ['size']

class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name='Spalva')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Prekės spalva'
        verbose_name_plural = 'Prekės spalvos'
        ordering = ['name']

class Clothing(models.Model):
    GENRE_CHOICES = [
        ('baby', 'Kūdikiams'),
        ('girls', 'Mergaitėms'),
        ('boys', 'Berniukams'),
        ('unisex', 'Unisex'),
    ]
    name = models.CharField(max_length=100, verbose_name='Pavadinimas')
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Kategorijos tipas')
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, verbose_name='Lytis')
    brand = models.CharField(max_length=100, verbose_name='Prekės ženklas', blank=True, null=True)
    description = HTMLField(verbose_name='Aprašymas', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Kaina')
    sizes = models.ManyToManyField(Size, verbose_name='Dydžiai', blank=True)
    colors = models.ManyToManyField(Color, verbose_name='Spalvos', blank=True)
    is_available = models.BooleanField(default=True, verbose_name='Ar prekė yra?')
    stock = models.PositiveIntegerField(verbose_name='Kiekis sandėlyje', default=0)
    is_on_sale = models.BooleanField(default=False, verbose_name="Ar išpardavime?")
    image = models.ImageField(upload_to='image/', blank=True, null=True, verbose_name='Nuotrauka')

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_product_type(self):
        return "Clothing"

    def get_price(self):
        return self.price

    class Meta:
        verbose_name = 'DRABUŽIAI'
        verbose_name_plural = 'DRABUŽIAI'

class Footwear(models.Model):
    GENRE_CHOICES = [
        ('baby', 'Kūdikiams'),
        ('girls', 'Mergaitėms'),
        ('boys', 'Berniukams'),
        ('unisex', 'Unisex'),
    ]
    name = models.CharField(max_length=100, verbose_name='Pavadinimas')
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Kategorijos tipas')
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, verbose_name='Lytis')
    brand = models.CharField(max_length=100, verbose_name='Prekės ženklas', blank=True, null=True)
    description = HTMLField(verbose_name='Aprašymas', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Kaina')
    sizes = models.ManyToManyField(Size, verbose_name='Dydžiai', blank=True)
    colors = models.ManyToManyField(Color, verbose_name='Spalvos', blank=True)
    is_available = models.BooleanField(default=True, verbose_name='Ar prekė yra?')
    stock = models.PositiveIntegerField(verbose_name='Kiekis sandėlyje', default=0)
    is_on_sale = models.BooleanField(default=False, verbose_name="Ar išpardavime?")
    image = models.ImageField(upload_to='image/', blank=True, null=True, verbose_name='Nuotrauka')

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_product_type(self):
        return "Footwear"

    def get_price(self):
        return self.price

    class Meta:
        verbose_name = 'AVALYNĖ'
        verbose_name_plural = 'AVALYNĖ'

class OtherProduct(models.Model):
    GENRE_CHOICES = [
        ('baby', 'Kūdikiams'),
        ('girls', 'Mergaitėms'),
        ('boys', 'Berniukams'),
        ('unisex', 'Unisex'),
    ]
    name = models.CharField(max_length=100, verbose_name='Pavadinimas')
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Kategorijos tipas')
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, verbose_name='Lytis')
    brand = models.CharField(max_length=100, verbose_name='Prekės ženklas', blank=True, null=True)
    description = HTMLField(verbose_name='Aprašymas', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Kaina')
    sizes = models.ManyToManyField(Size, verbose_name='Dydžiai', blank=True)
    colors = models.ManyToManyField(Color, verbose_name='Spalvos', blank=True)
    is_available = models.BooleanField(default=True, verbose_name='Ar prekė yra?')
    stock = models.PositiveIntegerField(verbose_name='Kiekis sandėlyje', default=1)
    is_on_sale = models.BooleanField(default=False, verbose_name="Ar išpardavime?")
    image = models.ImageField(upload_to='image/', blank=True, null=True, verbose_name='Nuotrauka')

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_product_type(self):
        return "OtherProduct"

    def get_price(self):
        return self.price

    class Meta:
        verbose_name = 'KITOS PREKĖS'
        verbose_name_plural = 'KITOS PREKĖS'

class ProductImage(models.Model):
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE, related_name='images', verbose_name='Drabužis', null=True, blank=True)
    footwear = models.ForeignKey(Footwear, on_delete=models.CASCADE, related_name='images', verbose_name='Avalynė', null=True, blank=True)
    otherproduct = models.ForeignKey(OtherProduct, on_delete=models.CASCADE, related_name='images', verbose_name='Kita', null=True, blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='Nuotrauka')

    class Meta:
        verbose_name = 'Prekės papildoma nuotrauka'
        verbose_name_plural = 'Prekės papildomos nuotraukos'

    def __str__(self):
        return f'Papildoma nuotrauka {self.id}'

class Review(models.Model):
    clothing = models.ForeignKey(Clothing, on_delete=models.CASCADE, related_name='reviews', verbose_name='Drabužis', null=True, blank=True)
    footwear = models.ForeignKey(Footwear, on_delete=models.CASCADE, related_name='reviews', verbose_name='Avalynė', null=True, blank=True)
    otherproduct = models.ForeignKey(OtherProduct, on_delete=models.CASCADE, related_name='reviews', verbose_name='Kita', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Vartotojas')
    rating = models.PositiveIntegerField(default=5, verbose_name='Įvertinimas')
    comment = models.TextField(verbose_name='Atsiliepimas', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')

    class Meta:
        verbose_name = 'Atsiliepimas'
        verbose_name_plural = 'Atsiliepimai'

    def __str__(self):
        return f'Atsiliepimas {self.user.username} apie {self.clothing or self.footwear or self.otherproduct}'
