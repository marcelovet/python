# requests para requisicoes http
# https://www.youtube.com/watch?v=Qd8JT0bnJGs&ab_channel=Ot%C3%A1vioMiranda
import requests

# se sem definir a port
# http:// -> 80
# https:// -> 443
url = "http://localhost:3000/"
response = requests.get(url)

print(response)
print(response.headers)
# print(response.content)
print(response.text)
