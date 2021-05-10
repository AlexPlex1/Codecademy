import csv
import json


compromised_users = []
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for item in password_csv:
    password_now = item
    # print(password_now['Username'])
    compromised_users.append(password_now['Username'])

# print(compromised_users)
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {'The Boss':'Mission Success'}
  json.dump(boss_message_dict, boss_message)

# testing if executed correctly and practicing reading json
# with open('boss_message.json') as boss_message:
#   t = json.load(boss_message)
#   print(t)

with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)

with open('new_passwords.csv') as new_passwords_obj:
  t = new_passwords_obj.read()
  print(t)
