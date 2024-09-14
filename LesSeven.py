import requests

url = 'https://httpbin.org/post'
data = {
    'custname': 'Elon Musk',
    'custtel': '+9989989989',
    'custemail': 'real_elon@mail.com',
    'size': 'large',
    'topping': 'cheese',
    'delivery': '21:00',
    'comment': 'I love pizza'

}

response = requests.post(url, data=data)
print(response)
