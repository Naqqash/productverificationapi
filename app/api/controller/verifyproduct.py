from app.api.database.db import product_exists


def VerifyProduct(productId):
    return product_exists(productId)
