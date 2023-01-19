import requests
import json

access_token = 'MmVmMDdhMDktMTdhYS00ZGNhLWI2ZTMtZTcwN2ZkNmNkODcyNDI5MzVhYzctZDAy_P0A1_f47c3c72-ce4d-4f2f-9d29-02816c42a704'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
