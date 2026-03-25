from fastapi import FastAPI
from proekt640 import proekt640AxmedovDilmurod
app = FastAPI()
@app.get("/")
def root():
    return{"message": "Hello gruppa 640"}

@app.get("/funcFIO")
def get_proekt640AxmedovDilmurod (x:int, y:int):
    return{"result": proekt640AxmedovDilmurod(x,y)}

