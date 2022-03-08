from django import urls
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import Settings, settings
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
