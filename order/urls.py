from django.urls import path
from . import views
urlpatterns = [
    path('order', views.orders , name='addOrder'),
    path('Cart', views.Carts , name='cart'),
    path('deleteOrder/<int:cartID>', views.deleteOrder , name='delOrder'),
    path('sumQuantity/<int:orderID>', views.sumQuantity , name='sumQuantity'),
    path('subQuantity/<int:orderID>', views.subQuantity , name='subQuantity'),
]
