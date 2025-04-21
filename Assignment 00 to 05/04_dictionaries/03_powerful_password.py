import hashlib
def main():
    print("Hsh Password Login System")
    print("Please enter your email and password to log in.")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(stored_logins, email, password_to_check):
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    else:
        return False

# Example usage
stored_logins = {
    "user@example.com": hash_password("mypassword123"),
    "admin@example.com": hash_password("adminpass"),
}

print(login(stored_logins, "user@example.com", "mypassword123"))  # True
print(login(stored_logins, "admin@example.com", "wrongpass"))     # False
print(login(stored_logins, "ghost@example.com", "anything"))      # False

if __name__ == "__main__":
    main()
