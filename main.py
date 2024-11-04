from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Model untuk data pengguna
class User(BaseModel):
    id: int
    name: str
    email: str

# Simulasi database
users_db: Dict[int, User] = {
    1: User(id=1, name="Eve", email="eve@example.com"),
    2: User(id=2, name="Frank", email="frank@example.com"),
}

# Endpoint untuk mendapatkan semua pengguna
@app.get("/users", response_model=List[User])
def fetch_all_users():
    return list(users_db.values())

# Endpoint untuk mendapatkan pengguna berdasarkan ID
@app.get("/users/{user_id}", response_model=User)
def fetch_user_by_id(user_id: int):
    if user_id in users_db:
        return users_db[user_id]
    raise HTTPException(status_code=404, detail="User not found")

# Endpoint untuk menambahkan pengguna baru
@app.post("/users", response_model=User)
def add_new_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User ID already exists")
    users_db[user.id] = user
    return user

# Endpoint untuk memperbarui pengguna yang ada
@app.put("/users/{user_id}", response_model=User)
def modify_existing_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return user

# Endpoint untuk menghapus pengguna berdasarkan ID
@app.delete("/users/{user_id}")
def remove_user(user_id: int):
    if user_id in users_db:
        del users_db[user_id]
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")