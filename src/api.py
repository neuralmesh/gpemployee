import logging
TAG = "#API"

logging.basicConfig(level=logging.DEBUG) 

def log(msg, tag=TAG):
    logging.debug("%s: %s", tag, str(msg)) 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import get_model

app = FastAPI()

class InputData(BaseModel):
    text: str

class OutputData(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"model": str(get_model())}

@app.post("/get_response", response_model=OutputData)
def get_response(data: InputData):
    log("data: %s".format(data))

    model = get_model()
    
    log("model: %s".format(model))

    model_response = model.get_response(data.text)
    
    log("model_response: %s".format(model_response))

    response = {"text": model_response}

    log("response: %s".format(model_response))

    return response

