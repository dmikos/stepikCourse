import simplecrypt

with open("passwords.txt", 'r') as passf, open("encrypted.bin", "rb") as dataf:
    data = dataf.read()
    for line in passf:
        try:
            text = simplecrypt.decrypt(line.rstrip(), data)
        except simplecrypt.DecryptionException:
            continue
        else:
            print(text.decode('utf8'))
            break
