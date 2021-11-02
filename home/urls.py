from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('cipher/',views.cipher,name='cipher'),
  path('menu_decipher/',views.menu_decipher,name='menu_decipher'),
  path('playfair/', views.playfair,name='playfair'),
  path('cesar/',views.cesar,name='cesar'),
]