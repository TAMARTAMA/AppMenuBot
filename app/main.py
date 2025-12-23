from fastapi import FastAPI
from app.api.router import api_router


app = FastAPI(
    title="WhatsApp Bot API",
    version="1.0.0"
)

app.include_router(api_router)

print("🚀 Server starting...")

@app.get("/")
def read_root():
    return {"message": "Welcome to the WhatsApp Bot API!"}