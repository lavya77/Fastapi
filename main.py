from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello!!!"

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product(id:int):
    for product in products:
        if product.id == id:
            return product
        
    return "product not found"

@app.post("/product")
def add_products(product:Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id:int , product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i]= product
            return "Product added successfulyy"
    return "no product added!"    

@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            products.remove(products[i]) # you can also write , del products[i]
            
            return "product deleted"

    return "No product deleted"        
    pass