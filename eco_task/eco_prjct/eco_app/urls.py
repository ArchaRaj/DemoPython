
from django.urls import path

from eco_app import views
from eco_prjct import settings
app_name='eco_app'
urlpatterns = [
    #path('',views.index,name="index")
    path('',views.allProductcat,name="allProductcat"),
    path('<slug:c_slug>/',views.allProductcat,name="products_by_category"),
    path('<slug:c_slug>/<slug:pro_slug>/',views.proDetail,name='procatdetail'),
]