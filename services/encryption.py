from hashlib import sha256

def generate_hash(value: str) -> str:
    return sha256(value.encode()).hexdigest()