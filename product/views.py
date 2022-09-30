from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

import product
from .models import Product, Rating
from django.utils import timezone
from .forms import ProductForm, RateForm
from django.shortcuts import get_object_or_404, render


class IndexView(generic.ListView):
    template_name = 'product/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_queryset(self):
        return Product.objects.filter(pub_date__lte=timezone.now())


class ProductCreate(generic.CreateView, generic.FormView):
    model = Product
    template_name = 'product/createform.html'
    form_class = ProductForm
    success_url = '/'


class ProductUpdate(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update.html'

    def get_success_url(self):
        return reverse('product:detail', kwargs={'pk': self.object.pk})


class ProductDelete(generic.DeleteView):
    model = Product
    template_name = 'product/delete.html'

    def get_success_url(self):
        return reverse('product:index')
