import tornado.ioloop
import tornado.web
import os

# Class Imports

from Classes.Authentication.Login import *
from Classes.Authentication.Register import *
from Classes.Token.GenerateToken import *
from Classes.Console.console import console

def make_app():
    return tornado.web.Application([
        (r"/Success/(.*)", GenerateToken),
        (r"/Register", Register),
        (r"/Login", Login),

        (r"/success/(.*)", GenerateToken),
        (r"/login", Login),
        (r"/register", Register),
    ])

if __name__ == "__main__":
    TokenDB.connect()
    console.info("Database connected.")

    if not os.path.exists("firstrun"):
        sqlhelpers.create_tables()
        with open("firstrun","w+") as f:
            f.write("a")

    app = make_app()
    app.listen(6969)
    console.info("Server has begun running in http://localhost:6969/")
    tornado.ioloop.IOLoop.current().start()
