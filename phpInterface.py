import requests
import json

class phpInterface:
    def __init__(self):
        self.__username = None
        self.__password = None
        self.__email = None
        self.__saveData = None

    def createNewUser(self, _username, _password, _email):
        userData = {"function":"create","userName": _username,"password": _password,"email":_email}
        url = 'http://localhost/newUser.php'
        print(userData)
        resp = requests.post(url, params = userData)
        data = resp.json()
        print(resp)
        parsed_json = json.loads(data)
        print(parsed_json['message'])
        print(parsed_json['username'])
