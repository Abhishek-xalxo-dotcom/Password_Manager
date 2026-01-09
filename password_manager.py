import hashlib

password_manager = {}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_account(username: str, password: str):
    if username in password_manager:
        return False, "Username already exists"

    password_manager[username] = hash_password(password)
    return True, "Account created successfully"

def login(username: str, password: str):
    hashed = hash_password(password)

    if username in password_manager and password_manager[username] == hashed:
        return True, "Login successful"
    return False, "Invalid username or password"
