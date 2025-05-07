from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional: Allow frontend access (adjust if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Lasavo backend is live"}

@app.get("/api/check_user")
def check_user(id: str):
    if id == "demo1":
        return {"status": "active"}
    else:
        return {"status": "inactive"}
