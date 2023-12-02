# src/main.py

from fastapi import FastAPI
from .model import model
app = FastAPI()

model = model.get_model()

@app.get("/")
def read_root():
    return {"model": str(model)}

