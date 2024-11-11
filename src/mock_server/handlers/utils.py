from typing import Optional


def get_server_status(container: str, data: str) -> Optional[str]:
    data_list = data.split("\n")
    for _ in data_list:
        if container in _:
            return _
        else:
            continue
    return f"Container {container} not found!"


def change_status_server(container: str, data: str, status: str) -> tuple[str, bool]:
    data_list = data.split("\n")
    resp = ""
    find_status = False
    for _ in data_list:
        if container in _:
            n = _.split(";")
            n[1] = f"\"{status}\"" if n[1] != f"\"{status}\"" else n[1]
            resp += f"{str(n).replace("', '", ";").removeprefix("['").removesuffix("']")}\n"
            find_status = True
            continue
        else:
            resp += f"{_}\n"
    return resp, find_status
