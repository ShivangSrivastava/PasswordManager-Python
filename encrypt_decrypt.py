try:
    import cryptocode
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'cryptocode'])

KEY = open("encryptionKey.txt").read()

def encode(string):
    return cryptocode.encrypt(string, KEY)


def decode(encoded):
    return cryptocode.decrypt(encoded, KEY)
