from Classes.Database import *

def CheckToken(Token):
    try:
        if sqlhelpers.check_token_presence(token=Token):
            sqlhelpers.remove_token(token=Token)
            return True
        return False
    except:
        return False