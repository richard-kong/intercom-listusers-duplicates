# -*- coding: utf-8 -*-
import requests

intercom_api_key = 'API_KEY'
intercom_app_id = 'APP_ID'
start_page = 1
end_page = 62

users = {}
emails = []
for i in range(start_page,end_page):
    payload = {'page': i, 'per_page': 50, 'sort':'created_at','order':'asc'}
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
            
        emails.append(user["email"])
            
for user in users:
     if len(users[user]) > 1:
         print "id = {0} pages = {1} ".format(user,str(users[user] ))

print "expected total users = {0}".format(response["total_count"])
print "unique emails = {0}".format(len(set(emails)))
print "unique ids = {0}".format(len(users))
print "total emails = {0}".format(len(emails))




    

