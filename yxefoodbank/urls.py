from django.contrib import admin
from django.urls import path, include
from account.views import (
    registration_view,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('store.urls')),
    path('register/', registration_view, name="register"),
]
