from .docker_manage_handler import DockerManage
from .root_handler import RootHandler


HANDLERS = (
    RootHandler,
    DockerManage,
)
