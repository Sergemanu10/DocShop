"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_card, cart, delete_cart
from accounts.views import signup, logout_user, login_user
from shop import settings

urlpatterns = [
    path('', index, name='index'), # Index
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'), # S'inscrire
    path('login/', login_user, name='login'), # Se connecter
    path('logout/', logout_user, name='logout'), # Se déconnecter
    path('cart/', cart, name='cart'), # Afficher les produits
    path('cart/delete/', delete_cart, name='delete-cart'), # Supprimer le panier
    path('product/<str:slug>/', product_detail, name="product"), # Ajouter les détails des produits
    path('product/<str:slug>/add-to-card/', add_to_card, name="add-to-card"),  # Ajouter les produits dans le panier
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
