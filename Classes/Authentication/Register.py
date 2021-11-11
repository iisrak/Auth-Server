import tornado.web
import json
from Classes.Database import *
from Classes.Authentication.Hashing.helpers import *
from Classes.Token.CheckToken import *

class Register(tornado.web.RequestHandler):

    def post(self):
        body = json.loads(self.request.body)
        username = body["username"]
        password = body["password"]
        token = body["token"]

        if (sqlhelpers.check_user_presence(username)):
            return self.write("2") # User already exists

        if (CheckToken(token) == False):
            return self.write("1") # Invalid token

        sqlhelpers.insert_new_user(username=username, password=helpers.hash_pass(password), token=token)

        return self.write("0") # Success