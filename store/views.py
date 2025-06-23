from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from store.models import Product, Order, Card


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={'product': product})




def add_to_card(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    card, _ = Card.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)


    if created:
        card.orders.add(order)
        card.save()
    else:
        order.quantity +=1
        order.save()


    return redirect(reverse("Product", kwargs={"slug":slug}))