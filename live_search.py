from django.core import serializers

def live_search(request):
    q = request.GET.get("q", "123123")
    products = Product.objects.all()
    for product in products:
        product.description += q
    products_json = serializers.serialize("json", products)
    return products_json