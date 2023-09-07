import tornado.web
import random
from Classes.Database import *
from string import ascii_letters

class GenerateToken(tornado.web.RequestHandler):
    def get(self, admintoken):
        if admintoken == "Admin":
            Token = ""

            for _ in range(30):
                Token += random.choice(ascii_letters + "0123456789")

            sqlhelpers.insert_token(token=Token)

            return self.write(Token)
        else:
            return self.redirect("https://www.youtube.com/watch?v=YZduI-_l6eQ") # Rick roll :)