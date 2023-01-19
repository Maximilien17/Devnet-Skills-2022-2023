import requests
import json

access_token = 'ZDE0YWRjMjgtMWRkMy00MjgyLTkxYmEtOTA2YjAxODNkMjIwYmRjNDY5YmYtZTdj_P0A1_f47c3c72-ce4d-4f2f-9d29-02816c42a704'
url = 'https://api.ciscospark.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'user@example.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))