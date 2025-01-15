from pydantic import BaseModel

class Product(BaseModel):
    product_id: str
    product_name: str
    product_rating: float
    number_of_reviews: int
    product_image_url: str
    product_category: str
    price_usd: int
    price_ngn: int