from locust import HttpLocust, TaskSet, task

import re

class UserBegavior(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        response = self.client.get("/login")

        csrf_param = re.search("<meta name=\"csrf-param\" content=\"([^\"]+)\" />", response.text).group(1)
        csrf_token = re.search("<meta name=\"csrf-token\" content=\"([^\"]+)\" />", response.text).group(1)

        self.client.post("/login", {"usermname": "admin", "password": "admin-password", csrf_param: csrf_token})

    def logout(self):
        response = self.client.get("/")

        csrf_param = re.search("<meta name=\"csrf-param\" content=\"([^\"]+)\" />", response.text).group(1)
        csrf_token = re.search("<meta name=\"csrf-token\" content=\"([^\"]+)\" />", response.text).group(1)

        self.client.post("/logout", {csrf_param: csrf_token})

    @task
    def top(self):
        self.client.get("/")

    @task(2)
    def mypage(self):
        with self.client.get("/my/page", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("not authenticated?")

    @task
    def projects(self):
        self.client.get("/projects")

class RedminUser(HttpLocust):
    task_set = UserBegavior
    min_wait = 500
    max_wait = 1000
