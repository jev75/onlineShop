from .models import Category

def categories(request):
    return {
        'categories': Category.objects.prefetch_related('subcategory_set').all()
    }
