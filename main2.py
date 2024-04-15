import requests

API_KEY = "d366c9479bcbd63c047d7e6b7b4b7233"
cidade = 'rio de janeiro'
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] -273.15
print(descricao, temperatura)