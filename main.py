import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr


class UserAdd(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLog(BaseModel):
    username: str
    password: str


users_db = {}

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/register", response_class=JSONResponse)
async def register(user: UserAdd):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    users_db[user.username] = {"email": user.email, "password": user.password}
    return {"message": "Пользователь зарегистрирован"}


@app.post("/login", response_class=JSONResponse)
async def login(user: UserLog):
    if user.username not in users_db or users_db[user.username]["password"] != user.password:
        raise HTTPException(status_code=400, detail="Неверное имя пользователя или пароль")
    return {"message": "Авторизация успешна!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
