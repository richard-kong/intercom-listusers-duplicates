# -*- coding: utf-8 -*-
import requests

intercom_api_key = 'API_KEY'
intercom_app_id = 'API_ID'
start_page = 1
end_page = 20

users = {}
for i in range(start_page,end_page):
    payload = {'page': i, 'per_page': 50}
    headers = {'Accept': 'application/json'}    
    r = requests.get('https://api.intercom.io/users', 
                     headers = headers,
                     auth = requests.auth.HTTPBasicAuth(intercom_app_id, intercom_api_key),
                     data = payload)
    response = r.json()
    
    for user in response["users"]:
        if user["id"] in  users:
            users[user["id"]].append(i)
        else:
            users[user["id"]] = [i]
            
            
for user in users:
     if len(users[user]) > 1:
         print "id = {0} pages = {1} ".format(user,str(users[user] ))

