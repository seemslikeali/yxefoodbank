from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Price, Donation
import stripe

# secret key shown in settings for access to stripe API
stripe.api_key = settings.STRIPE_SECRET_KEY


# HTML preview and variables to be used
class DonationLandingPageView(TemplateView):
    template_name = "donation.html"

    def get_context_data(self, **kwargs):
        # variables to go through in HTML from stored in SQL
        product = Donation.objects.get(name="Donation")
        prices = Price.objects.filter(product=product)
        context = super(DonationLandingPageView,
                        self).get_context_data(**kwargs)

        context.update({
            "prices": prices,
            "product": product
        })
        return context


# product payment page when selected from donation page
# has a successs page cancelation page. everything is logged per API in dashboard
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        # in production we change this to domain and not local host
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        # from stripe API documentaion
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            # pages are located in master templates
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        # return to success or cancelation page
        return redirect(checkout_session.url)


# cancalation view
class CancelView(TemplateView):
    template_name = "cancel.html"


# casuccess view
class SuccessView(TemplateView):
    template_name = "success.html"
