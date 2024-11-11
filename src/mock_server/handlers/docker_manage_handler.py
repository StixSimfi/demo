import asyncio
from http import HTTPStatus

from aiohttp.web_response import Response
from aiohttp.web_request import Request

from .base import Base
from .utils import get_server_status, change_status_server

# Токен забит гвоздями. В проде он генерируется на сервере администраторами.
TOKEN = '4f69baaf-a498-48a4-8275-405f8a10d175'


class DockerManage(Base):

    URL_PATH = r'/hooks/docker-qa-manage'

    @staticmethod
    async def get(request: Request) -> Response:
        if request.headers['X-Webhook-Token'] == TOKEN:
            # Используем плюшки прелести версии 3.10 :)
            match request.query["command"]:
                case  "ps":
                    resp = request.app.answer["ps"]
                    request.app.logger.debug(f"route {request.path} \n {resp}")
                    return Response(
                        text=resp
                    )
                case "status":
                    resp = get_server_status(request.query["container"], request.app.answer["ps"])
                    request.app.logger.debug(f"route {request.path} \n {resp}")
                    return Response(
                        text=resp
                    )
                case "restart":
                    resp, find = change_status_server(
                        request.query["container"],
                        request.app.answer["ps"],
                        "restarting")
                    request.app.logger.debug(f"route {request.path} \n {resp}")
                    request.app.answer["ps"] = resp.rstrip("\n")
                    await asyncio.sleep(5)
                    resp, find = change_status_server(
                        request.query["container"],
                        request.app.answer["ps"],
                        "running")
                    request.app.logger.debug(f"route {request.path} \n {resp}")
                    request.app.answer["ps"] = resp.rstrip("\n")
                    return Response(
                        text=(
                            f"{request.query["container"]} is restarting" if find
                            else f"Container {request.query["container"]} not found!"
                        )
                    )
                case "start":
                    resp, find = change_status_server(
                        request.query["container"],
                        request.app.answer["ps"],
                        "running")
                    request.app.logger.debug(f"route {request.path} \n {resp}")
                    request.app.answer["ps"] = resp.rstrip("\n")
                    return Response(
                        text=(
                            f"{request.query["container"]} is started" if find
                            else f"Container {request.query["container"]} not found!"
                        )
                    )
                case "stop":
                    resp, find = change_status_server(
                        request.query["container"],
                        request.app.answer["ps"],
                        "stopped")
                    request.app.logger.debug(f"route {request.path} \n {resp}")
                    request.app.answer["ps"] = resp.rstrip("\n")
                    return Response(
                        text=(
                            f"{request.query["container"]} is stoped" if find
                            else f"Container {request.query["container"]} not found!"
                        )
                    )
                case _:
                    return Response(text="BAD REQUEST", status=HTTPStatus.BAD_REQUEST)
