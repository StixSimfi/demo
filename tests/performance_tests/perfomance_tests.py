from locust import FastHttpUser, run_single_user, task # noqa


class TestUser(FastHttpUser):
    pass


"""
# Раскоментируйте для переключения locust в отладочный режим
if __name__ == "__main__":
    run_single_user(TestUser)
"""
