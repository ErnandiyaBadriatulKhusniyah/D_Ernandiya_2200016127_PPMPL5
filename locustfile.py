from locust import FastHttpUser, task, between

class UserSimulation(FastHttpUser):
    wait_time = between(1, 3)  # Delay antara setiap permintaan

    @task(3)
    def fetch_all_users(self):
        response = self.client.get("/users")
        print("Request GET /users", response.status_code)

    @task(2)
    def fetch_single_user(self):
        user_id = 1  # Ubah dengan ID pengguna yang akan diuji
        response = self.client.get(f"/users/{user_id}")
        print(f"Request GET /users/{user_id}", response.status_code)

    @task(1)
    def add_user(self):
        response = self.client.post("/users", json={"id": 3, "name": "Charlie", "email": "charlie@example.com"})
        print("Request POST /users", response.status_code)

    @task(1)
    def modify_user_info(self):
        user_id = 1  # Ubah dengan ID pengguna yang ingin diperbarui
        response = self.client.put(f"/users/{user_id}", json={"id": user_id, "name": "Alice Updated", "email": "alice_updated@example.com"})
        print(f"Request PUT /users/{user_id}", response.status_code)

    @task(1)
    def remove_user(self):
        user_id = 2  # Ubah dengan ID pengguna yang ingin dihapus
        response = self.client.delete(f"/users/{user_id}")
        print(f"Request DELETE /users/{user_id}", response.status_code)
