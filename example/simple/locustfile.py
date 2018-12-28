import time
from locust import Locust, TaskSet, task, HttpLocust
from tavern.core import run
from tavern.testutils.locust import TavernLocust

# class HTTPTaskSet(TaskSet):
#     @task
#     def t1(self):
#         self.client.get("/")
# class MyLocust(HttpLocust):
#     task_set = HTTPTaskSet
#     min_wait = 500
#     max_wait = 1500

class MyTaskSet(TaskSet):
    @task
    def task1(self):
        self.client.run_tavern_tests(filename="test_server.tavern.yaml", names_contain=["doubles"])

    @task
    def task2(self):
        self.client.run_tavern_tests(filename="test_server.tavern.yaml", names_contain=["error"])

    @task
    def task3(self):
        self.client.run_tavern_tests(filename="test_server.tavern.yaml", names_contain=["series"])


class MyLocust(TavernLocust):
    task_set = MyTaskSet
    min_wait = 500
    max_wait = 1500
