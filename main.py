import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = "abdulrazak"
GRAPH_ID = "graph1"
TOKEN = os.environ.get("TOKEN")
THANKS_CODE = os.environ.get("THANKS_CODE")


pixela_endpoint = "https://pixe.la/v1/users"

user_data = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": THANKS_CODE
}

# response = requests.post(url=pixela_endpoint, json=user_data)
# print(response.text)

create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

create_graph_data = {
    "id": "graph1",
    "name": "Reading",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=create_graph_endpoint, json=create_graph_data, headers=headers)
# print(response.text)

create_pixel_endpoint = f"{create_graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2023, month=3, day=16)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? ")
}

# response = requests.post(url=create_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

get_pixel_endpoint = f"{create_pixel_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.get(url=get_pixel_endpoint, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{create_pixel_endpoint}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "80"
}

# response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{create_pixel_endpoint}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)

delete_user_endpoint = f"{pixela_endpoint}/{USERNAME}"

# response = requests.delete(url=delete_user_endpoint, headers=headers)
# print(response.text)
