import hashlib

text = ('....')

sha256 = hashlib.sha256()
sha256.update(text.encode('utf-8'))

print(sha256.hexdigest())
