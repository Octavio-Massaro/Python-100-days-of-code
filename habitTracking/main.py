import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "enter your token"
USERNAME = "enter your username"
GRAPH_ID = "enter your graph_id"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
header = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "Hour",
    "type": "float",
    "color": "ajisai",

}
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4",
}
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=header)

