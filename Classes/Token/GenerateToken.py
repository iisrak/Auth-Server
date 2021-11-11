import tornado.web
import random, os
from Classes.Database import *

class GenerateToken(tornado.web.RequestHandler):
    global Char_Array

    Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    Char_Array = []

    for Character in Characters:
        Char_Array.append(Character)

    def get(self, admintoken):
        if admintoken == "Admin":
            Token = ""

            for i in range(30):
                Token += random.choice(Char_Array)

            sqlhelpers.insert_token(token=Token)

            return self.write(Token)
        else:
            return self.redirect("https://www.youtube.com/watch?v=YZduI-_l6eQ") # Rick roll :)