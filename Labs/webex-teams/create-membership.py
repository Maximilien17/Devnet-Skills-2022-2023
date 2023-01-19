import requests

access_token = 'MmVmMDdhMDktMTdhYS00ZGNhLWI2ZTMtZTcwN2ZkNmNkODcyNDI5MzVhYzctZDAy_P0A1_f47c3c72-ce4d-4f2f-9d29-02816c42a704'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNzZmZGQ0MzAtOGViMy0xMWVkLTg5NDUtMjUxYmU1YzY2ZDll'
person_email = 'benjamin.ghosez@student.odisee.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())