
from django.urls import reverse
from django.views import generic
from .models import Product
from django.utils import timezone
from .forms import ProductForm, RateForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "product/home.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "your Account has been successfully created")

        return redirect('product:signin')

    return render(request, "product/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'product/index.html', {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('product:home')

    return render(request, "product/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "logged out succesfully created")
    return redirect('product:home')


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
