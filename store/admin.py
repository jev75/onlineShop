from django.contrib import admin
from .models import Category, Subcategory, Size, Color, Clothing, Footwear, OtherProduct, Review, ProductImage
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size', 'category')
    search_fields = ('size', 'category__name')
    list_filter = ('category',)
    ordering = ['size']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image']

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_display', 'product_link', 'category', 'genre', 'brand', 'price', 'stock', 'is_on_sale', 'is_available']
    search_fields = ['name', 'description', 'brand']
    autocomplete_fields = ['category', 'sizes', 'colors']
    list_filter = ['category', 'brand', 'is_on_sale', 'is_available', 'genre']
    ordering = ['name']
    inlines = [ProductImageInline]

    fieldsets = (
        (None, {
            'fields': ['name', 'category', 'genre', 'brand', 'description', 'price', 'stock', 'is_on_sale', 'is_available', 'image']
        }),
        ('Sizes and Colors', {
            'fields': ['sizes', 'colors']
        }),
    )

    def thumbnail_display(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: auto;" />')
        return "Paveikslėlio nėra"

    thumbnail_display.short_description = 'Peržiūra'

    def product_link(self, obj):
        return format_html(f'<a href="/admin/store/{obj._meta.model_name}/{obj.id}/change/">{obj.name}</a>')

    product_link.short_description = 'Pavadinimas'

@admin.register(Footwear)
class FootwearAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_display', 'product_link', 'category', 'genre', 'brand', 'price', 'stock', 'is_on_sale', 'is_available']
    search_fields = ['name', 'description', 'brand']
    autocomplete_fields = ['category', 'sizes', 'colors']
    list_filter = ['category', 'brand', 'is_on_sale', 'is_available', 'genre']
    ordering = ['name']
    inlines = [ProductImageInline]

    fieldsets = (
        (None, {
            'fields': ['name', 'category', 'genre', 'brand', 'description', 'price', 'stock', 'is_on_sale', 'is_available', 'image']
        }),
        ('Sizes and Colors', {
            'fields': ['sizes', 'colors']
        }),
    )

    def thumbnail_display(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: auto;" />')
        return "Paveikslėlio nėra"

    thumbnail_display.short_description = 'Peržiūra'

    def product_link(self, obj):
        return format_html(f'<a href="/admin/store/{obj._meta.model_name}/{obj.id}/change/">{obj.name}</a>')

    product_link.short_description = 'Pavadinimas'

@admin.register(OtherProduct)
class OtherProductAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_display', 'product_link', 'category', 'genre', 'brand', 'price', 'stock', 'is_on_sale', 'is_available']
    search_fields = ['name', 'description', 'brand']
    autocomplete_fields = ['category', 'sizes', 'colors']
    list_filter = ['category', 'brand', 'is_on_sale', 'is_available', 'genre']
    ordering = ['name']
    inlines = [ProductImageInline]

    fieldsets = (
        (None, {
            'fields': ['name', 'category', 'genre', 'brand', 'description', 'price', 'stock', 'is_on_sale', 'is_available', 'image']
        }),
        ('Sizes and Colors', {
            'fields': ['sizes', 'colors']
        }),
    )

    def thumbnail_display(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 50px; height: auto;" />')
        return "Paveikslėlio nėra"

    thumbnail_display.short_description = 'Peržiūra'

    def product_link(self, obj):
        return format_html(f'<a href="/admin/store/{obj._meta.model_name}/{obj.id}/change/">{obj.name}</a>')

    product_link.short_description = 'Pavadinimas'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'user', 'rating', 'comment', 'created_at']
    search_fields = ['user__username', 'comment']
    list_filter = ['rating', 'created_at']

    def product_name(self, obj):
        return obj.clothing or obj.footwear or obj.otherproduct

    product_name.short_description = 'Prekė'

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'clothing', 'footwear', 'otherproduct', 'image']
    search_fields = ['clothing__name', 'footwear__name', 'otherproduct__name']
