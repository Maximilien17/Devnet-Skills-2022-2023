import json
import xlrd

groups_struc = {
 "groups": [
      { "group": { "group_id": "G-A" , "group_name": "DEVASC_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Noel", "email": "noel@odisee.be"},
                     {"person_id": "P-2" , "person_name": "Mary", "email": "mary@odisee.be"},
                     {"person_id": "P-3" , "person_name": "Jens", "email": "jens@odisee.be"} 
                   ]
                 }
      },
      { "group": { "group_id": "G-B" , "group_name": "DEVASC_B" ,    
                   "members": [   
                     {"person_id": "P-4" ,"person_name": "Ives", "email": "ives@odisee.be"}, 
                     {"person_id": "P-5" ,"person_name": "John", "email": "john@odisee.be"}, 
                     {"person_id": "P-6" ,"person_name": "Alec", "email": "alec@odisee.be"} 
                   ]     
                 }
      },
      { "group": { "group_id": "G-C" , "group_name": "DEVASC_C" ,    
                   "members": [   
                     {"person_id": "P-7" ,"person_name": "Matt", "email": "matt@odisee.be"}, 
                     {"person_id": "P-8" ,"person_name": "Paul", "email": "paul@odisee.be"}, 
                     {"person_id": "P-9" ,"person_name": "Elvi", "email": "elvi@odisee.be"} 
                   ] 
                 }
      }
   ]
}

wb = xlrd.open_workbook("webex_groups.xlsx")
sheet = wb.sheet_by_index(0)

groups_struc["group"] = sheet.cell_value(1, 0) 
groups_struc["person_name"]  = sheet.cell_value(1, 1)

groups_struc["email"] = sheet.cell_value(1, 2)
print(groups_struc)

groups_struc["group"] = sheet.cell_value(2, 0) 
groups_struc["person_name"]  = sheet.cell_value(2, 1)
groups_struc["email"] = sheet.cell_value(2, 2)
print(groups_struc)