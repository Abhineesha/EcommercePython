from django . urls import path
from . import views
app_name='shop'

urlpatterns=[
    path('',views.allProduct,name='allProduct'),
    path('shop/<slug:c_slug>/',views.allProduct,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodcatdetail'),

]