import hashlib, hmac


def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.

    Args:
        password (str): The plain text password.

    Returns:
        str: The hexadecimal SHA-256 hash of the password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def can_login(username: str, password: str, db: dict) -> bool:
    """
    Determines if a user can log in by verifying the username and password hash.

    Improvements:
    - Validates input types to prevent unexpected errors.
    - Rejects empty strings for username and password to avoid accidental logins.
    - Returns False if the username is missing from the database.
    - Uses constant-time comparison for password hashes to mitigate timing attacks.
    - Early returns improve readability.
    - Clear documentation added.

    Args:
        username (str): The username to check.
        password (str): The password to verify.
        db (dict): A dictionary mapping usernames to hashed passwords.

    Returns:
        bool: True if login is allowed, False otherwise.

    Example:
        >>> db = {"alice": hash_password("secret123")}
        >>> can_login("alice", "secret123", db)
        True
    """
    # Reject invalid types for username, password, or db
    if not isinstance(username, str) or not isinstance(password, str) or not isinstance(db, dict):
        return False
    # Reject empty username or password
    if not username.strip() or not password.strip():
        return False
    # Return False if username is missing from db
    if username not in db:
        return False
    # Hash the input password and compare with stored hash using constant-time comparison
    return hmac.compare_digest(db[username], hash_password(password))


# Example database with hashed passwords
user_db = {
    "alice": hash_password("password123"),
    "bob": hash_password("securepass"),
    "charlie": hash_password("mypassword"),
}


# Get username and password from user input
username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()

# Output result to user as True/False
print(can_login(username, password, user_db))

# --- Before (Original) ---
# def can_login(username, password, db):
#     if username in db and db[username] == password:
#         return True
#     else:
#         return False

# --- After (Reviewed) ---
# - Passwords are hashed for security.
# - Input types and empty strings are validated.
# - Early returns improve readability.
# - Constant-time comparison prevents timing attacks.
# - Documentation is clear and maintainable.