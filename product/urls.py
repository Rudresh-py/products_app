from django.template.defaulttags import url
from django.urls import path, reverse
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .models import Product

app_name = 'product'
urlpatterns = [
                  path('', views.IndexView.as_view(), name='index'),
                  path('create/', views.ProductCreate.as_view(), name='create'),
                  path('<int:pk>/detail/', views.ProductDetail.as_view(), name='detail'),
                  path('<int:pk>/update', views.ProductUpdate.as_view(), name='update'),
                  path('<int:pk>/delete/', views.ProductDelete.as_view(), name='delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
