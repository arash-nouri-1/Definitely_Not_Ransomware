from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
publickey = key.publickey()

with open("priv.key", "w") as file:
    file.write(key.export_key("PEM").decode())

with open("pub.key", "w") as file:
    file.write(publickey.export_key("PEM").decode())