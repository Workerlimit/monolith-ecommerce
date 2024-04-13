from locust import HttpUser, task, between
import json

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_products(self):
        self.client.get("/products")

    @task
    def add_product(self):
        product_data = {
            "productName": "Test Product",
            "price": 10.0,
            "description": "Test Description",
            "productImage": ""
        }
        self.client.post("/products", json=product_data)

    @task
    def delete_product(self):
        product_id = 1
        self.client.delete(f"/products/{product_id}")

    @task
    def add_product_with_image(self):
        product_data = {
            "productName": "Test Product with image",
            "price": 15.0,
            "description": "Test Description with image",
            "productImage": "https://images.squarespace-cdn.com/content/v1/5bf4bf814611a019a7c475f0/1562038085083-DLUD125WWPOUTGYD8Q60/ke17ZwdGBToddI8pDm48kHH9S2ID7_bpupQnTdrPcoF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0nQwvinDXPV4EYh2MRzm-RRB5rUELEv7EY2n0AZOrEupxpSyqbqKSgmzcCPWV5WMiQ/product%2Bphotography"
        }
        self.client.post("/products", json=product_data, headers={"Content-Type": "application/json"})

if __name__ == "__main__":
    import os
    os.environ.setdefault("LOCUST_MODE", "ForkingPickle")
    from locust.runners import MasterRunner, WorkerRunner

    if __name__ == '__main__':
        from locust.main import main
        main()