import requests

USERNAME = 'mountsamosn'
TOKEN = "aghhdfdf2ds23sd!@3 "
GRAPH_ID ="graph1"



pixela_endpoint = "https://pixe.la/v1/users "

user_params = {
    'tokens': TOKEN,
    'username': USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graph"

graph_config = {
    'id': GRAPH_ID,
    'name': "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}



headers = {
    "X-USER-TOKEN": TOKEN
}


response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/<graphID>'

pixel_data = {
    "data": "20200724",
    "quantity": "1000",
}
 
