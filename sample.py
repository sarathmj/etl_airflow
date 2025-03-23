import requests

def fetch_random_users(num_users=5):
    url = f"https://randomuser.me/api/?results={num_users}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']  # Returns a list of user dictionaries
    else:
        raise Exception(f"API request failed with status code: {response.status_code}")

# Test the function
if __name__ == "__main__":
    users = fetch_random_users(5)
    for user in users:
        print(f"Name: {user['name']['first']} {user['name']['last']}, Email: {user['email']}")