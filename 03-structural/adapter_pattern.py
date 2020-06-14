import os
import requests


class StatusClass:
    def status(self):
        pass


class User(StatusClass):
    def status(self):
        user = os.environ.get("USER") or os.environ.get("USERNAME")
        return f"Current user: {user}"


class Directory(StatusClass):
    def status(self):
        return f"Current working dir: {os.getcwd()}"


class InternetConnection:
    def check_connection_status(self):
        try:
            internet_ok = requests.get("https://google.com").status_code == 200
        except requests.exceptions.ConnectionError:
            internet_ok = False
        connection = "ok" if internet_ok else "offline"
        return f"Internet connection: {connection}"


class AdapterInternetConnection(StatusClass, InternetConnection):
    def status(self):
        return self.check_connection_status()


class Adapter2(StatusClass):
    def __init__(self, internet_connection: InternetConnection):
        self.internet_connection = internet_connection

    def status(self):
        return self.internet_connection.check_connection_status()


class CheckSystem:
    def __init__(self, system):
        self.system = system

    def status(self):
        print(self.system.status())


if __name__ == "__main__":
    internet_connection = InternetConnection()
    adapter_object = Adapter2(internet_connection)
    systems_list = [User(), Directory(), AdapterInternetConnection(), adapter_object]
    for system in systems_list:
        cs = CheckSystem(system)
        cs.status()
