from pickle import load
from encrypt_decrypt import decode


file1 = "password.bin"  # FTP stores
file2 = "user_details.bin"  # username password
file3 = "userdata.bin"  # empty


with open(file1, "rb") as f:
    while True:
        try:
            l = load(f)
        except EOFError:
            break
        d = eval(decode(l))
        print(d)
