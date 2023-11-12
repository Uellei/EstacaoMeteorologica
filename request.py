import requests

# Defina os dados que você deseja enviar
dados = {
    "Temperatura": "31",
    "Umidade": "20",
    "Luminosidade": "100",
    "Pressao": "100",
    "Rotacao": "18"
}
# dados = {

# }

# Defina a URL do endpoint onde o servidor Flask está escutando
url = 'http://192.168.15.10:5000/dados'  # Atualize com a URL do seu servidor Flask

# Faça uma solicitação POST para enviar os dados
response = requests.post(url, json=dados)

# Verifique a resposta do servidor
if response.status_code == 200:
    print('Dados enviados com sucesso')
else:
    print('Erro ao enviar os dados:', response.status_code)
