# Auth-Server
Web based login and register in python.
It uses tornado for the web server and peewee for the database.

# Endpoints
/success/[ADMINTOKEN] (get) -> Generates a new token\
/register (post username, password, token) -> Writes 3 (exception error), 2 (username already exists), 1 (invalid token), 0 (success)\
/login (post username, password) -> Writes 2 (exception error), 1 (incorrect login), 0 (success)