from fastapi import FastAPI ,Depends
from models import Product
from database import session ,engine
import database_models
from sqlalchemy.orm import Session


app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello!!!"

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db= session()

    count = db.query(database_models.Product).count

    if count == 0:
        for product in products:
         db.add(database_models.Product("product.model_dump"))

    db.commit()

init_db()       

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):

    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product(id:int ,db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id ==id ).first()
    if product:
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
            products.remove(products[i]) # you can also write , del products
            
            return "product deleted"

    return "No product deleted"        
    