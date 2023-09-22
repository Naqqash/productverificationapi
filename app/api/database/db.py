from pymongo import MongoClient
from fastapi import HTTPException

from app.core.config import settings

client = MongoClient(settings.dbUrl)
db = client["naqqash-test"]
collection = db["productslist"]


def add_product(product_id: str, product_name: str):
    try:
        collection.insert_one({"_id": product_id, "name": product_name})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def product_exists(product_id: str):
    result = bool(collection.find_one({"_id": product_id}))
    return result


def delete_product(product_id: str):
    result = collection.delete_one({"_id": product_id})
    return result.deleted_count > 0
