from fastapi import FastAPI
from .model import get_model
app = FastAPI()

model = get_model()

@app.get("/")
def read_root():
    return {"model": str(model)}

