from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from products.models import Product
import json

# Create your views here.

def add_to_cart(request):
    product_id = request.POST["product"]
    quantity = int(request.POST["quantity"])
    
    cart = request.session.get("cart", {}) # If variable name "cart" is in session, give it back to me (nb. session is a dictionary). If not, give me an empty dictionary. Finally, save it in cart.
    cart[product_id] = cart.get(product_id, 0) + quantity # See if a line item in cart exists for that product id, if not default to zero. If there is, add additional quantity. Finally, save it in cart[product_id].
    request.session["cart"] = cart 
    
    return redirect("/")
    
    
def remove_from_cart(request):
    product_id = request.POST['product']

    cart = request.session.get('cart', {})
    del cart[product_id]

    request.session['cart'] = cart

    return redirect("/cart/view/")    
   
   
    
def view_cart(request):
    cart = request.session.get('cart', {})
    
    cart_items = []
    cart_total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'brand': product.brand,
            'sku': product.sku,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'stock': product.stock,
            'quantity': quantity,
            'total': item_total
        })
        cart_total += item_total

    return render(request, "cart/view_cart.html", {'cart_items': cart_items, 'cart_total': cart_total})