import requests

def get_random_user():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    data = response.json()
    print("Name:", data["results"][0]["name"])
    print("Email:", data["results"][0]["email"])

if __name__ == "__main__":
    get_random_user()
