import tornado.ioloop
import tornado.web

# Class Imports

from Classes.Token.GenerateToken import *
from Classes.Authentication.Register import *
from Classes.Authentication.Login import *

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

    if not os.path.exists("firstrun"):
        sqlhelpers.create_tables()
        with open("firstrun","w") as f:
            f.write("a")

    app = make_app()
    print("Created app.")
    app.listen(6969)
    print("Beginning.")
    tornado.ioloop.IOLoop.current().start()
