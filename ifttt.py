import requests

url = 'https://maker.ifttt.com/trigger/redes/with/key/<KEY>'
myobj = {'value1': 'segunda', 'value2': 'teste', 'value3': 'xyz'}

x = requests.post(url, data = myobj)

if x.status_code == 200:
    print(x.text)
else:
    print("Error")
    print(x.status_code)
