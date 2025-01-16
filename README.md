# ProductHub API

ProductHub is a RESTful API that provides real-time e-commerce product data scraped from websites like Amazon and eBay. Developers can easily access product details such as name, price, image URL, and category, making it perfect for building price comparison tools, product discovery platforms, and more.

## 🌟 Features
- **Real-time Product Data**: Get up-to-date product information from top e-commerce platforms.
- **Category Filtering**: Browse products by category.
- **Search Functionality**: Search products using keywords.
- **Customizable Limits**: Control how many items to fetch with a simple query parameter.
- **Developer-Friendly Documentation**: Easy-to-understand API docs and integration guides.

## 🚀 Live Demo
Access the live API: https://ancient-marti-mz-scripter-730e4701.koyeb.app/

## ⚙️ Installation
1. Clone the Repository
   ```
   git clone https://github.com/your_username/producthub.git
   cd producthub
   ```
2. Install Dependencies
   ```
   pip install -r requirements.txt
   ```
3. Run the Server
   ```
   uvicorn app.main:app --reload
   ```

## Deploy on Koyeb
- Push your code to GitHub.
- Connect the repo on [Koyeb](https://www.koyeb.com/)
- Set the build command to `uvicorn app.main:app --host 0.0.0.0`.

## 📃 License
This project is licensed under the MIT License.
