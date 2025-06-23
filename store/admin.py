from django.contrib import admin
from store.models import Product, Order, Card

"""
Enregister le modèle 
"""

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Card)