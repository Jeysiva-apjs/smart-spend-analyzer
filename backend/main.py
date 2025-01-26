import config
from fastapi import FastAPI
from routes import crud
import uvicorn


app = FastAPI()

@app.get("/")
def check_running():
    return {"message": "Server is up and running."}

app.include_router(crud.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)