from aiohttp.web_urldispatcher import View


class Base(View):
    URL_PATH: str
