
import requests
import json

class php_interface:

    def __init__(self):
        x=1


    # send a request to php files on the database to see if the user name
    # or email address already exists in the database
    # a true value means return a true to the log_in function that calls this
    # method. Then no new user is created
    def userNameAndEmailExist():
        x=1

    # Send a requesto to php files on the database to create a new user
    # with the arguments received by this function. When the process is complete
    # a new confirmation code is sent.
    def createNewUser(x,y):
        data = {'username':x,'password':y}
        createUserUrl = 'http://localhost/test.php'

        r = requests.get(createUserUrl, params = data)
