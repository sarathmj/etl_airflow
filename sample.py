import requests
import json

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
    users = fetch_random_users(1)
    # print(type(users))
    
    # Serializing json
    json_object = json.dumps(users, indent=4)
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
        

    
    # for user in users:
    #     print(f"Name: {user['name']['first']} {user['name']['last']}, Email: {user['email']}")