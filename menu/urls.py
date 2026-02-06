from django.urls import path
from . import views
from .views import TacosAPI, PizzaAPI, BoissonAPI, ContactAPI

urlpatterns = [
    path('', views.index, name='index'),
    path('api/tacos/', TacosAPI.as_view(), name='api-tacos'),
    path('api/pizzas/', PizzaAPI.as_view(), name='api-pizzas'),
    path('api/boissons/', BoissonAPI.as_view(), name='api-boissons'),
    path('api/contact/', ContactAPI.as_view(), name='api-contact'),
    #upload image supabase
    path('upload/', views.upload_tacos, name='upload_tacos'),
    
]
