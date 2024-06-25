from itertools import chain
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Clothing, Footwear, OtherProduct, Review, Subcategory, Category
from .forms import ReviewForm

class HomeView(generic.ListView):
    template_name = 'store/home.html'
    context_object_name = 'latest_products'

    def get_queryset(self):
        clothing = Clothing.objects.order_by('-id')[:3]
        footwear = Footwear.objects.order_by('-id')[:3]
        otherproduct = OtherProduct.objects.order_by('-id')[:3]
        return list(chain(clothing, footwear, otherproduct))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = self.get_queryset()
        context['categories'] = Category.objects.prefetch_related('subcategory_set').all()
        return context

class ClothingListView(generic.ListView):
    model = Clothing
    template_name = 'store/clothing_list.html'
    context_object_name = 'clothing_list'

class ClothingDetailView(generic.DetailView):
    model = Clothing
    template_name = 'store/clothing_detail.html'
    context_object_name = 'clothing_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['reviews'] = self.object.reviews.all()
        context['images'] = self.object.images.all()
        context['colors'] = self.object.colors.all()  # Pridėta, kad būtų galima pasirinkti spalvas
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.clothing = self.object
            review.user = request.user
            review.save()
            return redirect('store:clothing_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

class FootwearListView(generic.ListView):
    model = Footwear
    template_name = 'store/footwear_list.html'
    context_object_name = 'footwear_list'

class FootwearDetailView(generic.DetailView):
    model = Footwear
    template_name = 'store/footwear_detail.html'
    context_object_name = 'footwear_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['reviews'] = self.object.reviews.all()
        context['images'] = self.object.images.all()
        context['colors'] = self.object.colors.all()  # Pridėta, kad būtų galima pasirinkti spalvas
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.footwear = self.object
            review.user = request.user
            review.save()
            return redirect('store:footwear_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

class OtherProductListView(generic.ListView):
    model = OtherProduct
    template_name = 'store/otherproduct_list.html'
    context_object_name = 'otherproduct_list'

class OtherProductDetailView(generic.DetailView):
    model = OtherProduct
    template_name = 'store/otherproduct_detail.html'
    context_object_name = 'otherproduct_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['reviews'] = self.object.reviews.all()
        context['images'] = self.object.images.all()
        context['colors'] = self.object.colors.all()  # Pridėta, kad būtų galima pasirinkti spalvas
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.otherproduct = self.object
            review.user = request.user
            review.save()
            return redirect('store:otherproduct_detail', pk=self.object.pk)
        return self.get(request, *args, **kwargs)

class ProductsBySubcategoryView(generic.ListView):
    template_name = 'store/products_by_subcategory.html'
    context_object_name = 'products'

    def get_queryset(self):
        subcategory = get_object_or_404(Subcategory, id=self.kwargs['subcategory_id'])
        clothing = Clothing.objects.filter(category=subcategory)
        footwear = Footwear.objects.filter(category=subcategory)
        other_products = OtherProduct.objects.filter(category=subcategory)
        return list(chain(clothing, footwear, other_products))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = get_object_or_404(Subcategory, id=self.kwargs['subcategory_id'])
        return context
