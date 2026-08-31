from fastapi import FastAPI

app = FastAPI()

# Ek simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World! Meri API chal rahi hai."}

# Ek dynamic endpoint jisme parameter pass hota hai
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}