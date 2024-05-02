from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/")
def hello():
    return{"Hello There":"World of Pakistan"}
