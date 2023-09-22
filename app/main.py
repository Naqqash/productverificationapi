from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.api.database.db import add_product, product_exists, delete_product
from app.api.model.response import VerificationResponseSchema
from app.core.config import settings


app = FastAPI()
# Define CORS origins based on settings
origins = [
    # Replace with your actual allowed origins
    origin.strip()
    for origin in settings.origins.split(",")
]

# Add CORS middleware to allow specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Product(BaseModel):
    product_id: str
    product_name: str


@app.post("/add_product", response_model=None)
def create_product(product: Product):
    add_product(product.product_id, product.product_name)
    return {"message": "Product added successfully"}


@app.get("/verify")
def check_product_exists(code: str = Query(..., description="Product ID to check")):
    status = product_exists(code)
    print(status, code)
    if not status:
        raise HTTPException(status_code=404, detail="Not a verified product")
    else:
        return {"status": status}


@app.delete("/delete_product", response_model=bool)
def remove_product(product_id: str = Query(..., description="Product ID to delete")):
    return delete_product(product_id)
