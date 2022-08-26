from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUS"),
    path("tracker/",views.tracker,name="TrekkingStatus"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.productView,name="ProductView"),
    path("checkout/",views.checkout,name="Checkout")
]