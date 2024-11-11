import aiohttp
from typing import (Dict, List)
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

URL = "http://mock:8089/hooks/docker-qa-manage"
HEADERS = {"X-Webhook-Token": "4f69baaf-a498-48a4-8275-405f8a10d175"}
PARAMS = [
    "containerName",
    "containerStatus",
    "startTime",
    "imageName",
    "upTime",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def convert_string_to_dict(req: str) -> List[Dict]:
    str_list: List = req.replace("\"", "").split("\n")
    str_list.remove(str_list[len(str_list)-1]) if str_list[len(str_list)-1] == "" else str_list
    for i in range(0, len(str_list)):
        str_list[i] = str_list[i].split(";")
    for elem in range(0, len(str_list)):
        elem_dict = {}
        for i in range(0, len(str_list[elem])):
            elem_dict[PARAMS[i]] = str_list[elem][i]
        str_list[elem] = elem_dict
    print(str_list)
    return str_list


@app.get("/api/docker-qa-manage/ps")
async def get_list_container(request: Request) -> Dict:
    try:
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            async with session.get(f"{URL}?command=ps") as resp:
                print(await resp.text())
                if resp.status == 200:
                    return {
                        "status": "success",
                        "containers": await convert_string_to_dict(await resp.text())
                    }
    except aiohttp.client_exceptions.ClientConnectorDNSError:
        return {
            "status": "Remote server not found"
        }
    except Exception as __err:
        return {
            "status": __err
        }


@app.get("/api/docker-qa-manage/{command}/{container_name}")
async def change_status(command: str, container_name: str) -> Dict:
    try:
        query: str = f"?command={command}&container={container_name}"
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            async with session.get(f"{URL}{query}") as resp:
                if resp.status == 200:
                    return {
                        "status": "success",
                        "command": command
                    }
    except aiohttp.client_exceptions.ClientConnectorDNSError:
        return {
            "status": "Remote server not found"
        }
    except Exception as __err:
        return {
            "status": __err
        }
