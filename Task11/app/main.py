from fastapi import FastAPI, HTTPException, Response
from schemas import UserCreate, UserResponse


app = FastAPI()

db = {}


@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    user_id = len(db) + 1

    db[user_id] = {
        "username": user.username,
        "age": user.age
    }

    return UserResponse(
        id=user_id,
        username=user.username,
        age=user.age
    )


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(
        id=user_id,
        username=db[user_id]["username"],
        age=db[user_id]["age"]
    )


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")

    del db[user_id]

    return Response(status_code=204)