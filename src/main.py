import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles




main_app = FastAPI()
main_app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

@main_app.get('/')
def hello_world(request: Request):
    return templates.TemplateResponse('start.html', {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True)
