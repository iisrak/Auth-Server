import tornado.web
import json
from Classes.Database import *
from Classes.Authentication.Hashing.helpers import *

class Login(tornado.web.RequestHandler):

    def post(self):
        try:
            body = json.loads(self.request.body)
            username = body["username"]
            password = body["password"]
            info = sqlhelpers.get_user_object_from_username(username=username)
            if helpers.verify_pass(password, info["Password"]):
                return self.write("0") # Success
            return self.write("1") # Incorrect Login
        except:
            return self.write("2") # Exception error