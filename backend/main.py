from pathlib import Path
import sys
from fastapi import FastAPI
from routes import crud

parent_dir = str(Path(__file__).resolve().parent.parent)
print(parent_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
    

app = FastAPI()

@app.get("/")
def check_running():
    return {"message": "Server is up and running."}

app.include_router(crud.router)
