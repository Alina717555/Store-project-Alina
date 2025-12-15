from django.urls import path
from storeProducts.views import products, index, basket_add, basket_remove

app_name = 'storeProducts'
urlpatterns = [
    path('', index, name='main'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),

    # Products
    path('products/', products, name='products'),
    path('products/page/<int:page_number>/', products, name='products_page'),

    # Category products
    path('products/category/<int:category_id>/', products, name='category'),
    path('products/category/<int:category_id>/page/<int:page_number>/', products, name='category_page'),
]
