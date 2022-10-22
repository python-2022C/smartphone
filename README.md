# Smartphone 
## List of brands

- [ ] Apple
- [ ] Samsung
- [ ] Huawei
- [ ] Xiaomi
- [ ] Oppo
- [ ] Vivo
- [ ] Nokia

## Structure of the project
### 1. Design of the project database
### 2. Design of the project interface
### 3. Design of the project test
### 4. Design of the project report
### 5. Design of the project presentation

## List of tasks
### 1. Design of the project database
- [x] Create the database
- [x] Create the tables
- [ ] Create the relations
- [x] Create the views

### 2. Design of the project interface

- [ ] Create the interface
- [ ] Create the forms
- [ ] Create the reports

### 3. Design of API endpoints
- [ ] Create the API endpoints
- [ ] Create the API documentation

### 4. List of API endpoints

- [ ] GET /api/brands # Get all brands
- [ ] GET /api/brands/{id} # Get a brand
- [ ] POST /api/brands # Create a brand
- [ ] POST /api/brands/{id} # Update a brand
- [ ] DELETE /api/brands/{id} # Delete a brand


# List of task
- [x] Create the project

```django-admin startproject smartphone .```

- [x] Create the app

```python manage.py startapp smartphone_app```

- [x] Create the django's project database

```bash
python manage.py migrate
```

- [x] Create the superuser

```python manage.py createsuperuser```

- [x] Create the smartphone's app database tables

## Database schema
### 1. Brand
| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| name | varchar(255) | NO | | NULL | |
| company | varchar(255) | NO | | NULL | |
| color | varchar(255) | NO | | NULL | |
| RAM | int(11) | NO | | NULL | |
| memory | int(11) | NO | | NULL | |
| price | int(11) | NO | | NULL | |
| created_at | datetime | NO | | NULL | |
| updated_at | datetime | NO | | NULL | |
| img_url | varchar(255) | NO | | NULL | |

- [x] Create the smartphone's app database models

```python
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    RAM = models.IntegerField()
    memory = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img_url = models.CharField(max_length=255)
    def __str__(self):
        return self.name
```

- [x] Register the smartphone's app database models to the django admin



```python
from django.contrib import admin
from .models import Product
admin.site.register(Product)
```

- [x] Register the smartphone's app to the django's project

```python
INSTALLED_APPS = [
    'smartphone_app.apps.SmartphoneAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- [x] Create the smartphone's app database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


## Create the views of the smartphone's app
### 1. Create the view of the list of products


```python
from django.http import JsonResponse

def get_products(request):
    """
    Get all products
    args:
        request: the request object
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 2. Create the view of the detail of a product
```python
def get_product(request, id):
    """
    Get a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """

    return JsonResponse({'product': {}})
```
### 3. Create the view of the creation of a product

```python
def create_product(request):
    """
    Create a product
    args:
        request: the request object
    return:
        JsonResponse: the product
    """

    return JsonResponse({'product': {}})
```

### 4. Create the view of the update of a product

```python

def update_product(request, id):
    """
    Update a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    return JsonResponse({'product': {}})
```

### 5. Create the view of the deletion of a product

```python
def delete_product(request, id):
    """
    Delete a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    return JsonResponse({'product': {}})
```

# Add the product to the database using the curl command
```bash
curl -X POST -d "name=Samsung Galaxy S21&company=Samsung&color=Black&RAM=8&memory=128&price=1000&img_url=https://www.samsung.com/galaxy-s21_gallery_01.jpg" http://localhost:8000/add_product
```

# run the server
```bash
python manage.py runserver
```
# run the server in the local network
```bash
python manage.py runserver 0.0.0.0:8000
```


## List of views for querying the database
### 1. Create the view of the list of products by company

```python

def get_products_by_company(request, company):
    """
    Get all products by company
    args:
        request: the request object
        company: the company of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 2. Create the view of the list of products by color

```python
def get_products_by_color(request, color):
    """
    Get all products by color
    args:
        request: the request object
        color: the color of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 3. Create the view of the list of products by RAM

```python
def get_products_by_RAM(request, RAM):
    """
    Get all products by RAM
    args:
        request: the request object
        RAM: the RAM of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 4. Create the view of the list of products by memory

```python
def get_products_by_memory(request, memory):
    """
    Get all products by memory
    args:
        request: the request object
        memory: the memory of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 5. Create the view of the list of products by price

```python
def get_products_by_price(request, price):
    """
    Get all products by price
    args:
        request: the request object
        price: the price of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 6. Create the view of the list of products by price range

```python
def get_products_by_price_range(request, min_price, max_price):
    """
    Get all products by price range
    args:
        request: the request object
        min_price: the min price of the product
        max_price: the max price of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 7. Create the view of the list of products by RAM and memory

```python
def get_products_by_RAM_and_memory(request, RAM, memory):
    """
    Get all products by RAM and memory
    args:
        request: the request object
        RAM: the RAM of the product
        memory: the memory of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 8. Create the view of the list of products by RAM range
    
```python
def get_products_by_RAM_range(request, min_RAM, max_RAM):
    """
    Get all products by RAM range
    args:
        request: the request object
        min_RAM: the min RAM of the product
        max_RAM: the max RAM of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 9. Create the view of the list of products by memory range

```python
def get_products_by_memory_range(request, min_memory, max_memory):
    """
    Get all products by memory range
    args:
        request: the request object
        min_memory: the min memory of the product
        max_memory: the max memory of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 10. Create the view of the list of products by date

```python
def get_products_by_date(request, date):
    """
    Get all products by date
    args:
        request: the request object
        date: the date of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```

### 11. Create the view of the list of products by date range

```python
def get_products_by_date_range(request, min_date, max_date):
    """
    Get all products by date range
    args:
        request: the request object
        min_date: the min date of the product
        max_date: the max date of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```
### 12. Find the product by multiple companies

```python
def get_products_by_multiple_companies(request, companies):
    """
    Get all products by multiple companies
    args:
        request: the request object
        companies: the companies of the product
    return:
        JsonResponse: the list of products
    """

    return JsonResponse({'products': []})
```
