import requests

# url = "http://127.0.0.1:5001//Canteen/AddItem"

# payload = {'Name': 'Samosa',
# 'Price': '10'}
# files=[

# ]
# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)

# url = "http://127.0.0.1:5001//Canteen/AddImage/gffd"

# payload = {}
# files=[
#   ('Image',('untitled2.png',open('/D:/cHOBNK V2/untitled2.png','rb'),'image/png'))
# ]
# headers = {}

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)


Menu=[
  {'Name': 'Samosa','Price': '10','Image':"D:/College-Management/Images/Samosa.jpeg"},
  {'Name': 'Patis','Price': '10','Image':"D:/College-Management/Images/Patis.avif"},
  {'Name': 'Chicken Lollipop','Price': '30','Image':"D:/College-Management/Images/Chicken Lollipop.webp"},
  {'Name': 'Batata Vada','Price': '10','Image':"D:/College-Management/Images/Batata Vada.jpg"},
  {'Name': 'Mirchi','Price': '5','Image':"D:/College-Management/Images/Mirchi.jpg"},
  {'Name': 'Veg Fried Rice','Price': '80','Image':"D:/College-Management/Images/Veg Fried Rice.jpg"},
  {'Name': 'Chicken Fried Rice','Price': '100','Image':"D:/College-Management/Images/Chicken Fried Rice.png"},
  {'Name': 'Noodles','Price': '80','Image':"D:/College-Management/Images/Noodles.webp"},
  {'Name': 'Tea','Price': '15','Image':"D:/College-Management/Images/Tea.jpeg"},
  {'Name': 'Coffee','Price': '15','Image':"D:/College-Management/Images/Coffee.jpg"},
  
]

for Item in Menu:
  payload = {'Name': Item['Name'],'Price': Item['Price']}
  response = requests.request("POST", 'http://127.0.0.1:5001//Canteen/AddItem', data={'Name': Item['Name'],'Price': Item['Price']})
  print(response.text)
  url = "http://127.0.0.1:5001//Canteen/AddImage/gffd"


  files=[
    ('Image',(f"Item['Name'].png",open(Item['Image'],'rb'),'image/png'))
  ]
  response = requests.request("POST", f"http://127.0.0.1:5001//Canteen/AddImage/{Item['Name']}", files=files)
  print(response.text)
  
print('Done')