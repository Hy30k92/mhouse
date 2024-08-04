from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# 라우터 생성
mh_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')

@mh_router.get("/mh", response_class=HTMLResponse)
async def mh(req: Request):
    return templates.TemplateResponse('min/mh.html', {'request': req})

@mh_router.get("/semi", response_class=HTMLResponse)
async def semi(req: Request):
    return templates.TemplateResponse('min/semi.html', {'request': req})