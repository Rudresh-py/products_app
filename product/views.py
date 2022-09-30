import json
from django.shortcuts import render_to_response
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


# def rating(request, pk):
#     product = get_object_or_404(Product, pk)
#     try:
#         selected_rate = product.rating_set.get(pk=request.POST['rating'])
#     except (KeyError, Rating.DoesNotExist):
#         return render(request, 'product/rating.html',
#                       {'product': product, 'error_message': "you didnt select a choice"})
#
#     else:
#         selected_rate.rating += 1
#         selected_rate.save()
#     return HttpResponseRedirect(reverse('product:index', args=(product.id,)))


# def rate(request, pk):
#     if request.method == 'POST':
#         form = RateForm(pk=request.POST, instance=product)
#         if form.is_valid():
#             rate = form.save(commit=False)
#             rate.user = request.user
#             rate.save()
#             return render(request, 'product/rating.html')
#         else:
#             return HttpResponseRedirect(reverse('product:index', args=(product.id,)))
from django.views.generic.base import View
from .models import MyObject

class RateMyObjectView(View):

    def post(self, request):

        my_object = MyObject.objects.all().last()

        xhr = 'xhr' in request.GET
        star_value = request.POST.get('value', '')

        my_object.score = star_value
        my_object.save()

        response_data = {
            'message': 'value of star rating:',
            'value': star_value
        }

        if xhr and star_value:
            response_data.update({'success': True})

        else:
            response_data.update({'success': False})

        if xhr:
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        return render_to_response(sel, response_data)
