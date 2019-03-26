from django.urls import path
from . import views

app_name = 'koskas1_app'


urlpatterns = [
path('', views.index, name='index'),
path('contact', views.contact, name='contact'),
path('references', views.references, name='references'),
path('nos_prestation', views.nos_prestation, name='nos_prestation'),
path('travaux/<int:product_id>', views.product, name='product'),
] 