from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Price, Donation
import stripe


# Create your views here.


stripe.api_key = settings.STRIPE_SECRET_KEY


class DonationLandingPageView(TemplateView):
    template_name = "donation.html"

    def get_context_data(self, **kwargs):
        product = Donation.objects.get(name="Donation")
        prices = Price.objects.filter(product=product)
        context = super(DonationLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)


class CancelView(TemplateView):
    template_name = "cancel.html"


class SuccessView(TemplateView):
    template_name = "success.html"
