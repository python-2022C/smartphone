from django.http import JsonResponse
from .models import Product

# Define the function convert_to_json
def convert_to_json(product):
    """
    Convert a product to a JSON object
    args:
        product: a product object
    returns:
        a JSON object
    """
    product_json = {
        'id': product.id,
        'name': product.name,
        'company': product.company,
        'color': product.color,
        'RAM': product.RAM,
        'memory': product.memory,
        'price': product.price,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
        'img_url': product.img_url,
    }
    return product_json
    
def get_products(request):
    """
    Get all products
    args:
        request: the request object
    return:
        JsonResponse: the list of products
    """
    products = Product.objects.all()
    products_json = []
    for product in products:
        products_json.append(convert_to_json(product))


    return JsonResponse({'products': products_json})


def get_product(request, id):
    """
    Get a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    if request.method == 'GET':

        
        product = Product.objects.get(id=id)

        #Check if the product exists using the id    
        product_json = convert_to_json(product)
    

    return JsonResponse({'product': product_json})


def add_product(request):
    """
    Create a product
    args:
        request: the request object
    return:
        JsonResponse: the product
    """
    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST['name'],
            company=request.POST['company'],
            color=request.POST['color'],
            RAM=request.POST['RAM'],
            memory=request.POST['memory'],
            price=request.POST['price'],
            img_url=request.POST['img_url'],
        )
        product_json = convert_to_json(product)
        product.save() # save the product to the database
        
        return JsonResponse({'product': product_json})

    return JsonResponse({'product': {}})

def update_product(request, id):
    """
    Update a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        # product.name = request.POST['name']
        # product.company = request.POST['company']
        # product.color = request.POST['color']
        # product.RAM = request.POST['RAM']
        # product.memory = request.POST['memory']
        product.price = request.POST['price']
        # product.img_url = request.POST['img_url']
        product.save()
    return JsonResponse({'product': {}})


def delete_product(request, id):
    """
    Delete a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        product.delete()
    return JsonResponse({'product': {}})



def get_products_by_company(request, company):
    """
    Get all products by company
    args:
        request: the request object
        company: the company of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        products = Product.objects.filter(company=company)
        products_json = []
        for product in products:
            products_json.append(convert_to_json(product))

    return JsonResponse({'products': products_json})

def get_products_color(request,color):
    if request.method == 'GET':
        products = Product.objects.filter(color=color)
        products_json = []
        for product in products:
            products_json.append(convert_to_json(product))
    
    return JsonResponse({'products': products_json})