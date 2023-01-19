import requests

access_token = 'MmVmMDdhMDktMTdhYS00ZGNhLWI2ZTMtZTcwN2ZkNmNkODcyNDI5MzVhYzctZDAy_P0A1_f47c3c72-ce4d-4f2f-9d29-02816c42a704'
room_id = 'your_room_id'
message = 'T entends cque je suis entrain de faire la zebi? skinny de quoi'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'. format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())