from fastapi import FastAPI, APIRouter
from app.core.routes import auth, users

api = APIRouter(prefix="/api")
app = FastAPI()

api.include_router(auth.router)
api.include_router(users.router)

app.include_router(api)


@app.get("/")
def index():
    return "wellcome"
