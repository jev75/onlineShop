import requests

# Vartotojo prisijungimo duomenys
username = 'admin'
password = '1234'

# Gaukite naują prieigos žetoną
token_response = requests.post('http://127.0.0.1:8000/api/token/', data={
    'username': username,
    'password': password
})

if token_response.status_code == 200:
    token_data = token_response.json()
    access_token = token_data.get('access')

    # Naudokite žetoną API užklausai
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get('http://127.0.0.1:8000/api/orders/', headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Klaida: {response.status_code} - {response.text}")
else:
    print(f"Klaida gauti žetoną: {token_response.status_code} - {token_response.text}")
