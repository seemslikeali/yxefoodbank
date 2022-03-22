from django.urls import URLPattern, path
from . import views


urlpatterns = [
    # main store page
    path('store/', views.store, name="store"),
    path('checkout/', views.checkout, name="checkout"),
]
