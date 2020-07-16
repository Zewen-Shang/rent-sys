import hashlib
import time

def getHash(hash_key):
    md5 = hashlib.md5()
    md5.update(str(time.time()).encode("utf-8"))
    for x in hash_key:
        md5.update(str(x).encode("utf-8"))
    return md5.hexdigest()