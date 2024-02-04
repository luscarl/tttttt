import requests
    
auth_url = "https://ticktick.com/oauth/authorize"
params = {
    "response_type": "code",
    'scope': 'tasks:write',
    "client_id": 'wXN3hhG82Nd4pg41jI'
}
response = requests.get(auth_url, params=params)
print(response)