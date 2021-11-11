from argon2 import PasswordHasher

class Helpers():
    def __init__(self):
        self.passhasher = PasswordHasher()

    def hash_pass(self, password):
        return self.passhasher.hash(password)

    def verify_pass(self, password, currenthash):
        try:
            self.passhasher.verify(currenthash, password)
            return True
        except:
            return False

helpers = Helpers()