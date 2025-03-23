import requests

def extract_data(**kwargs):
    num_users = 1  # Adjustable
    url = f"https://randomuser.me/api/?results={num_users}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()['results']
        kwargs['ti'].xcom_push(key='extracted_data', value=data)
        print(f"Extracted {len(data)} users from the API")
    else:
        raise Exception(f"API request failed with status code: {response.status_code}")