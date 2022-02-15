from os import listdir
import os
import eml_parser
import datetime
import json
import re



while True:
    
    direct = input('Please enter the directory containing the EML files: ')
    
    try:
    
        directory_items= os.listdir(direct)
        break
    
    except:
    
        print('\nInvalid Directory Path. ')
        continue

print('\nFiles Found:\n')

for item in directory_items:
    
    print(item)
    
input('\nPress Enter to Continue...\n')
    
    
    

def json_serial(obj):
    
      if isinstance(obj, datetime.datetime):
            
            serial = obj.isoformat()
            
            return serial
        
for item in directory_items:
    
    try:
        
        with open(r'{}\{}'.format(direct,item), 'rb') as fhdl:
    
            raw_email = fhdl.read()
    

        ep = eml_parser.EmlParser()
        parsed_eml = ep.decode_email_bytes(raw_email)

        eml_data = json.dumps(parsed_eml, default=json_serial)



#Finds the index of the string requested
#eml_data.find('envelope-from')
#eml_data.find('from')

#regular expression for valid emails

        regex = r'envelope-from <\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        regex2 = r'("from": "(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)")'
        valid_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#finds all emails in the parsed eml
        email_list = re.findall(regex2,eml_data)


        target = email_list[0]

        target_email = target[1]

        print(target_email)
        
    except:
        
        print("NOT AN EML FILE")

#target_email = re.findall(valid_email,target)

#----------------------------------------------------------------
#  IGNORE BELOW: JUST TESTING 
#-----------------------------------------------------------------

#print(email_list)

#target_email = email_list[0]

#target_email = target_email.split('<')

#target_email = target_email[1]

#target_email
#eml_data[8918:8932]

#-----------------------------------------------------------------