import simplecrypt as f
with open("passwords.txt") as pw:
    passwords = pw.read().splitlines()

with open("encrypted.bin", 'rb') as file:
    encrypted = file.read()

for i in passwords:
    try:
        note = f.decrypt(i, encrypted).decode('utf8')
    except f.DecryptionException:
        pass
    else:
        print(note)