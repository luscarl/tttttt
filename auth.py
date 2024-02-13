# import requests
    
# auth_url = "https://ticktick.com/oauth/authorize"
# params = {
#     "response_type": "code",
#     'scope': 'tasks:write',
#     "client_id": 'wXN3hhG82Nd4pg41jI'
# }
# response = requests.get(auth_url, params=params)
# print(response)

from pprint import pprint
from notion_client import Client

notion_token = 'secret_4EcPpN6LGd8cxncbvF765z7fTBrwqC1goyqAYtEMpw0'
notion_page_id = '8571975d8d9d49d581eca261c06daf51'



def main():
    client = Client(auth=notion_token)

    page_response = client.pages.retrieve(notion_page_id)

    pprint(page_response, indent=2)

def write_text(client, page_id, text, type):
    Client.block.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": type,
                type: {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": text
                            }
                        }
                    ]
                }
            }
        ]
    )

if __name__ == '__main__':
    main()
    write_text('ae8f0b77-72ac-4408-96fc-8b54ea973520', notion_page_id, 'nteo', 'to_do')
          