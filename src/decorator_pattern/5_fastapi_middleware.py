from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from starlette.types import ASGIApp


async def index(request):
    return PlainTextResponse("index")


routes = [
    Route("/", endpoint=index),
]


class CustomMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, name: str):
        super().__init__(app)
        self.name = name

    async def dispatch(self, request, call_next):
        print(f"before {self.name}")
        response = await call_next(request)
        print(f"after {self.name}")
        return response


# 1. 앱 생성시에 파라미터로 전달
middleware = [
    Middleware(CustomMiddleware, name="A"),
    Middleware(CustomMiddleware, name="B"),
]

app = Starlette(routes=routes, middleware=middleware)

# 2. 앱에서 제공하는 메서드 활용
app.add_middleware(CustomMiddleware, name="C")


# 3. 앱에서 제공하는 데코레이터 활용
@app.middleware("http")
async def custom_middleware(request: Request, call_next):
    print("before D")
    response = await call_next(request)
    print("after D")
    return response
