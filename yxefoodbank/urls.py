from django import urls
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import Settings, settings
from django.urls import path, include
from account.views import registration_view
from userHist import views
from donation.views import (SuccessView,
                            CancelView, CreateCheckoutSessionView, DonationLandingPageView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('store.urls')),
    path('', include('userHist.urls')),
    path('donation/', DonationLandingPageView.as_view(), name="donationpage"),
    path('success/', SuccessView.as_view(), name='success'),
    path('register/', registration_view, name="register"),
    path('create-checkout-session/<pk>/',
         CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('cancel/', CancelView.as_view(), name='cancel'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
