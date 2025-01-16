from fastapi import FastAPI
from app.routes import products

app = FastAPI(title="ProductHub API", version="1.0.0", description="E-commerce Product Data API")

# Include product routes
app.include_router(products.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to ProductHub API"}