from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('customer', views.customer , name='customer'),
    path('order', views.order , name='order'),
    path('addcoffee', views.addcoffee , name='addcoffee'),
    path('<int:userid>/', views.customeraction , name='customeraction'),

]
