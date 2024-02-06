# import requests
    
# auth_url = "https://ticktick.com/oauth/authorize"
# params = {
#     "response_type": "code",
#     'scope': 'tasks:write',
#     "client_id": 'wXN3hhG82Nd4pg41jI'
# }
# response = requests.get(auth_url, params=params)
# print(response)

from notion_client import Client
from pprint import pprint

notion_token = 'secret_4EcPpN6LGd8cxncbvF765z7fTBrwqC1goyqAYtEMpw0'
notion_page_id = '379bd5a210194bf095758068fa1b3fb9'

def main():
    client = Client(auth=notion_token)

    page_response = client.pages.retrieve(notion_page_id)

    pprint(page_response, indent=2)

if __name__ == '__main__':
    main()
          