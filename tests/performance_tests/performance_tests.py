from locust import FastHttpUser, run_single_user, task, between # noqa
from tests.config import _BACKEND_HOST, _BACKEND_PORT


class TestUser(FastHttpUser):
    wait_time = between(0.5, 1.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(20)
    def get_list_container(self):
        self.client.get(f"/api/docker-qa-manage/ps")

    @task(2)
    def send_start_command(self):
        self.client.get(f"/api/docker-qa-manage/start/rabbit")

    @task(2)
    def send_stop_command(self):
        self.client.get(f"/api/docker-qa-manage/stop/rabbit")

    @task(1)
    def send_restart_command(self):
        self.client.get(f"/api/docker-qa-manage/restart/rabbit")


"""
# Раскоментируйте для переключения locust в отладочный режим
if __name__ == "__main__":
    run_single_user(TestUser)
"""
