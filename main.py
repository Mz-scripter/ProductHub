from fastapi import FastAPI
from app.routes import products
from fastapi.responses import FileResponse
import os

app = FastAPI(title="ProductHub API", version="1.0.0", description="E-commerce Product Data API")

# Include product routes
app.include_router(products.router)

@app.get("/")
async def read_root():
    file_path = os.path.join("app", "static", "documentation.html")
    return FileResponse(file_path, media_type='text/html')