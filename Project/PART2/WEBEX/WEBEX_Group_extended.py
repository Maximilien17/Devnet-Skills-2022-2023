import json

groups_struc = {
 "groups": [
      { "group": { "group_id": "G-A" 
                 , "group_name": "DEVASC_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Noel", "email": "noel@odisee.be"},
                     {"person_id": "P-2" , "person_name": "Mary", "email": "mary@odisee.be"},
                     {"person_id": "P-3" , "person_name": "Jens", "email": "jens@odisee.be"} 
                   ]
                 }
      },
      { "group": { "group_id": "G-B" 
                 , "group_name": "DEVASC_B" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Ives", "email": "ives@odisee.be"}, 
                     {"person_id": "P-5" ,"person_name": "John", "email": "john@odisee.be"}, 
                     {"person_id": "P-6" ,"person_name": "Alec", "email": "alec@odisee.be"} 
                   ]     
                 }
      },
      { "group": { "group_id": "G-C" , 
                   "group_name": "DEVASC_C" ,    
                   "members": [   
                     {"person_id": "P-7" ,"person_name": "Matt", "email": "matt@odisee.be"}, 
                     {"person_id": "P-8" ,"person_name": "Paul", "email": "paul@odisee.be"}, 
                     {"person_id": "P-9" ,"person_name": "Elvi", "email": "elvi@odisee.be"} 
                   ] 
                 }
      }
   ]
}


print('------1---------')
print(type(groups_struc))
print(groups_struc)
print('------1A--------')
# convert dict into json string
js_groups = json.dumps(groups_struc)
print(type(js_groups))
print(js_groups)
#print(json.dumps(groups_struc, indent=2))

print('------2---------')
for grp in groups_struc["groups"]:
    print('------2A--------')
    print(type(grp))
    print(grp)
    print('------2B--------')
    print(grp["group"]["group_name"])
    print('------2C--------')
    for per in grp["group"]["members"]:
        print(per["person_name"] + " => " + per["email"])
            
print('------3---------')
print(groups_struc.keys())
print('------3A---------')
print(groups_struc["groups"][0].keys())
print('------3B---------')
print(groups_struc["groups"][0]["group"].keys())
print('------3C---------')
print(groups_struc["groups"][0]["group"]["members"][0].keys())

import json
js_groups = json.dumps(groups_struc)
print(json.dumps(groups_struc, indent=2))

import yaml
yaml_data = yaml.dump(groups_struc)
print(yaml_data)

from dicttoxml import dicttoxml
xml_data = dicttoxml(groups_struc)
print(xml_data)
