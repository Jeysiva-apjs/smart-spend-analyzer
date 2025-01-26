import config
from fastapi import FastAPI
from routes import crud

app = FastAPI()

@app.get("/")
def check_running():
    return {"message": "Server is up and running."}

app.include_router(crud.router)
