from aiohttp.web import Response
from aiohttp.web import Request
from .base import Base


class RootHandler(Base):
    URL_PATH = r'/'

    @staticmethod
    async def get(request: Request) -> Response:
        resp = "mock server is running"
        request.app.logger.debug(f"route {request.path} \n {resp}")
        return Response(
            text=resp
        )
