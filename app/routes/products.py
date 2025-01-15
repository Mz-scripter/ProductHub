from fastapi import APIRouter, HTTPException, Query
from app.models.product import Product
from app.utils.data_loader import products_data
import random

router = APIRouter()


# Get all products (limit optional)
@router.get("/products", response_model=list[Product])
async def get_all_products(limit: int = Query(10, ge=1)):
    MAX_LIMIT = 100
    limit = min(limit, MAX_LIMIT)
    return products_data[:limit]

# Get available categories
@router.get("/products/categories", response_model=list[str])
def get_product_categories():
    return list(set([p['product_category'] for p in products_data]))

# Search for products
@router.get("/products/search", response_model=list[Product])
async def search_products(query: str = Query(..., min_length=3), limit: int = Query(10, ge=1)):
    MAX_LIMIT = 100
    limit = min(limit, MAX_LIMIT)

    matched_products = [
        product for product in products_data
        if query.lower() in product["product_name"].lower() or query.lower() in product["product_category"].lower()
    ]

    if not matched_products:
        raise HTTPException(
            status_code=404,
            detail={
                "error": f"No products found for query '{query}'. Please try a different search term."
            }
        )
    return matched_products[:limit]

# Get products by category
@router.get("/products/{category}", response_model=list[Product])
def get_products_by_category(category: str, limit: int = Query(10, ge=1)):
    MAX_LIMIT = 100
    limit = min(limit, MAX_LIMIT)
    category_products = [p for p in products_data if p['product_category'].lower() == category.lower()]
    if not category_products:
        raise HTTPException(status_code=404, detail={
            "error": f"Category '{category} not found. Use /products/categories to view available categories"
            })
    return category_products[:limit]

# Get a random product in a category
@router.get("/products/{category}/random", response_model=Product)
def get_random_product(category: str):
    category_products = [p for p in products_data if p['product_category'].lower() == category.lower()]
    if not category_products:
        raise HTTPException(status_code=404, detail={
            "error": f"Category '{category} not found. Use /products/categories to view available categories"
            })
    return random.choice(category_products)

# Get a product by ID
@router.get("/product/{product_id}", response_model=Product)
def get_product_by_id(product_id: str):
    for product in products_data:
        if product['product_id'] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

