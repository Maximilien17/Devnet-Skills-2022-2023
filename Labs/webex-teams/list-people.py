import requests
import json

access_token = 'MmVmMDdhMDktMTdhYS00ZGNhLWI2ZTMtZTcwN2ZkNmNkODcyNDI5MzVhYzctZDAy_P0A1_f47c3c72-ce4d-4f2f-9d29-02816c42a704'
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS81MzgwM2FhNi0wNDFiLTQ0YjktODc2ZS1kYTEwZmM0MjVjM2Q'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'. format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))