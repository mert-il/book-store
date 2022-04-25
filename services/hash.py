from hashlib import sha256

def generate_hash(value):
    return sha256(value.encode("utf-8")).hexdigest()