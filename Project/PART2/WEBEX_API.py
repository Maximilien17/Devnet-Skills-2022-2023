current_access_token = "ZTM3YmRlZGMtMGRkOC00YWQyLWFmNjctMGQxMTcwOGE1Yzc2ZTcyMjc3NjAtMWU3_P0A1_f47c3c72-ce4d-4f2f-9d29-02816c42a704"

import requests
import json

groups_struc = {
 "groups": [
      { "group": { "group_id": "G-A" 
                 , "group_name": "DEVASC_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Noel", "email": "noel@odisee.be", "Phone_number": "+32 487 30 75 97"},
                     {"person_id": "P-2" , "person_name": "Mary", "email": "mary@odisee.be", "Phone_number": "+32 487 85 75 45"},
                     {"person_id": "P-3" , "person_name": "Jens", "email": "jens@odisee.be", "Phone_number": "+32 127 85 55 67"} 
                   ]
                 }
      },
      { "group": { "group_id": "G-B" 
                 , "group_name": "DEVASC_B" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Ives", "email": "ives@odisee.be", "Phone_number": "+32 487 85 75 97"}, 
                     {"person_id": "P-5" ,"person_name": "John", "email": "john@odisee.be", "Phone_number": "+32 177 16 87 85"}, 
                     {"person_id": "P-6" ,"person_name": "Alec", "email": "alec@odisee.be", "Phone_number": "+32 675 45 68 77"} 
                   ]     
                 }
      },
      { "group": { "group_id": "G-C" , 
                   "group_name": "DEVASC_C" ,    
                   "members": [   
                     {"person_id": "P-7" ,"person_name": "Matt", "email": "matt@odisee.be", "Phone_number": "+32 382 85 10 11"}, 
                     {"person_id": "P-8" ,"person_name": "Paul", "email": "paul@odisee.be", "Phone_number": "+32 487 66 55 10"}, 
                     {"person_id": "P-9" ,"person_name": "Elvi", "email": "elvi@odisee.be", "Phone_number": "+32 399 56 66 16"} 
                   ] 
                 }
      }
   ]
}

from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(access_token = current_access_token)

print("Creating spaces +  members --> from Excel spreadsheet in the previous cell")
access_token = current_access_token 


def main2():
   
    url = 'https://api.ciscospark.com/v1/rooms'

    headers = { 'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type': 'application/json' }

    for rec in groups_struc["groups"]:
        create_group_name = rec["group"]["group_name"]
        payload_space = {"title": create_group_name}

        if payload_space["title"] != None:

            res_space = requests.post(url, headers=headers, json=payload_space)
 
            if res_space.status_code < 300:

                NEW_SPACE_ID = res_space.json()["id"]
 
                for mbr in rec["group"]["members"]:

                    room_id = NEW_SPACE_ID

                    person_email = mbr["email"] 

                    url2 = 'https://api.ciscospark.com/v1/memberships'

                    payload_member = {'roomId': room_id, 'personEmail': person_email}

                    res_member = requests.post(url2, headers=headers, json=payload_member)


def main():

    for rec in groups_struc["groups"]:

        demo_room = api.rooms.create(rec["group"]["group_name"])
      for email in rec["group"]["members"]:
            api.memberships.create(demo_room.id, personEmail=email["email"])


#### execute main() when called directly        

if __name__ == "__main__":
    main2() ### or main()



