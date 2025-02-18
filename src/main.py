import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from api.routers import main_router

main_app = FastAPI()

main_app.include_router(main_router)
main_app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@main_app.get('/')
def hello_world(request: Request):
    return templates.TemplateResponse('start.html', {'request': request})


@main_app.get("/informatika")
def informatika(request: Request):
    return templates.TemplateResponse('start_informatika.html', {'request': request})


if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True)
