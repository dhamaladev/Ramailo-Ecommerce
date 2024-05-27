from products.models import ProductModel
from products.serializers import ProductSerializer
import requests

url = "https://fakestoreapi.com/products"

# load data from given url
def load_data_from_api():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for product_data in data:
            product = ProductModel(
                title=product_data["title"],
                price=product_data["price"],
                description=product_data["description"],
                category=product_data["category"],
                image=product_data["image"],
                rating_rate = product_data["rating"]["rate"],
                rating_count = product_data["rating"]["count"],
            )
            product.save()
            print(f"Product {product_data['title']} created")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

load_data_from_api()
