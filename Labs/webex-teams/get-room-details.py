import requests

access_token = 'MmVmMDdhMDktMTdhYS00ZGNhLWI2ZTMtZTcwN2ZkNmNkODcyNDI5MzVhYzctZDAy_P0A1_f47c3c72-ce4d-4f2f-9d29-02816c42a704'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNzZmZGQ0MzAtOGViMy0xMWVkLTg5NDUtMjUxYmU1YzY2ZDll'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())