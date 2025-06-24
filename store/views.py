from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from store.models import Product, Order, Card


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={'product': product})



# Ajouter les produits dans le panier
def add_to_card(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    card, _ = Card.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)


    if created:
        card.orders.add(order)
        card.save()
    else:
        order.quantity +=1
        order.save()


    return redirect(reverse("product", kwargs={"slug": slug}))



# Afficher les produits
def cart(request):
    cart = get_object_or_404(Card, user=request.user)
    return render(request, 'store/cart.html', context={"orders": cart.orders.all()})

# Supprimer le panier
def delete_cart(request):
    if cart := request.user.card:
        cart.delete()

    return redirect('index')
