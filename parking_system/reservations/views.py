"""Reservation app views placeholder."""

import json
import os

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import stripe

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")


def index(request):
    return HttpResponse("Coin Parking API placeholder")


@csrf_exempt
def create_payment_intent(request):
    """Create a Stripe PaymentIntent using the provided amount."""
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    try:
        data = json.loads(request.body.decode())
        amount = int(data.get("amount"))
    except Exception:
        return JsonResponse({"error": "invalid amount"}, status=400)
    intent = stripe.PaymentIntent.create(amount=amount, currency="jpy")
    return JsonResponse({"clientSecret": intent.client_secret})


@login_required
def dashboard(request):
    return HttpResponse("Admin dashboard")
