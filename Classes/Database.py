from peewee import *
from playhouse.shortcuts import model_to_dict
from Classes.Console.console import *
TokenDB = SqliteDatabase("Tokens.db")

class BaseModel(Model):
    class Meta:
        database = TokenDB

#Tables

class CreateToken(BaseModel):
    Token = CharField()

class User(BaseModel):
    Username = CharField()
    Password = CharField()
    Token = CharField()

#Tables End

class SQLhelpers():
    def create_tables(self):
        with TokenDB:
            TokenDB.create_tables([CreateToken, User])
            console.info("Created Tables Okay")

    def insert_token(self, token):
        CreateToken.insert({
            CreateToken.Token: token
        }).execute()
        console.info("Inserted new token\n" + token)

    def remove_token(self, token):
            CreateToken.get(CreateToken.Token == token).delete_instance()
            console.info("Removed token\n" + token)

    def check_token_presence(self, token):
        try:
            CreateToken.get(CreateToken.Token == token)
            console.info("Token exists\n" + token)
            return True
        except:
            console.warning("Token doesn't exist\n" + token)
            return False

    def insert_new_user(self, username, password, token):
        User.insert({
            User.Username: username,
            User.Password: password,
            User.Token: token
        }).execute()
        console.info(f"Created a new user: \n{username}\n{password}\n{token}")

    def check_user_presence(self, user):
        try:
            User.get(User.Username == user)
            console.info("Username found\n" + user)
            return True
        except:
            console.warning("Username not found\n" + user)
            return False

    def get_user_object_from_username(self, username):
        return model_to_dict(User.get(User.Username == username))

    def get_user_object_from_token(self, token):
        return model_to_dict(User.get(User.Token == token))

sqlhelpers = SQLhelpers()