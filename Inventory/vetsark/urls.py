from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stock', views.stock, name='stock'),
    path('addstock', views.add_stock, name='addstock'),
    # path('add', views.addstock, name='add'),
    path('addcategory', views.add_category, name='addcategory'),
    # path('newcategory', views.new_category, name='newcategory'),

    # path('purchase', views.purchase, name='purchase'),
]