from hashlib import sha256

def generate_hash(password):
    return sha256(password.encode("utf-8")).hexdigest()