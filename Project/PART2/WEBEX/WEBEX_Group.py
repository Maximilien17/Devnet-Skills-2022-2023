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

resp_a1 = groups_struc["groups"][0]["group"]["group_name"]
resp_a2 = groups_struc["groups"][0]["group"]["members"][0]["person_name"]
print(resp_a1)
print(resp_a2)
resp_b1 = groups_struc["groups"][1]["group"]["group_name"]
resp_b2 = groups_struc["groups"][1]["group"]["members"][0]["person_name"]
print(resp_b1)
print(resp_b2)
for g in groups_struc["groups"]:
    print(g["group"]["group_name"])
    for p in g["group"]["members"]:
        print(p["person_name"] + " => " + p["Phone_number"] )

