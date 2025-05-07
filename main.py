# main.py
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

# Example list of authorized user IDs
authorized_users = {"demo1", "demo2", "demo3"}

@app.get("/api/check_user")
async def check_user(id: str = Query(..., description="User ID to check")):
    if id in authorized_users:
        return "ok"
    else:
        raise HTTPException(status_code=403, detail="Unauthorized")

@app.get("/")
def root():
    return {"message": "Lasavo backend is live"}
