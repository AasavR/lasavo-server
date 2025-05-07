# main.py
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

# Example list of authorized user IDs
authorized_users = {"demo1", "demo2", "demo3"}


@app.get("/api/check_user")
def check_user(id: str):
    # Temporary mock response
    if id == "demo1":
        return {"status": "active"}
    else:
        return {"status": "inactive"}

@app.get("/")
def root():
    return {"message": "Lasavo backend is live"}
