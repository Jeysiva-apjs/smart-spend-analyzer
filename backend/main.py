from fastapi import FastAPI
from routes import crud
    
app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Server is up and running."}

app.include_router(crud.router)
