
def items_in_cart(request):
    cart = request.session.get("cart", {})
    return {"items_in_cart": len(cart)}