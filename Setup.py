
import json

import requests

url = "http://127.0.0.1:5001//Signup"

payload = json.dumps({
  "Username": "Admin",
  "Email": "Admin@dbcegoa.ac.in",
  "Password": "4236541283462873562890651235708354612354238956237412896423752395627835287534653",
  "UserType": "Admin"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


# // Add Canteen Items