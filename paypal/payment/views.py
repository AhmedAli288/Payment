from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *


# Create your views here.

def simpleCheckout(request):
    return render(request, 'payment/simple_checkout.html')


def store(request):
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'payment/store.html', context)


def checkout(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product': product}

    return render(request, 'payment/checkout.html', context)


def paymentComplete(request):
    body = json.loads(request.body)

    # order = Order.objects.first()
    #
    # orderid = Order.objects.get(id=body['orderId'])

    product = Product.objects.get(id=body['productId'])

    order = Order.objects.create(
        product=product
    )

    print('Body:', body)
    response = {
        'order_id': order.id,
        'product_id': product.id,
        'message': 'Payment Completed!'
    }

    return JsonResponse(response)
