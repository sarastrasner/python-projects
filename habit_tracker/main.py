import requests
import datetime
USERNAME = "strassy"
TOKEN = "jhgjhgjg8o773"
GRAPH_ID = "graph1"

pixela_parameters = {
    "token": "jhgjhgjg8o773",
    "username": "strassy",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = 'https://pixe.la/v1/users'

# CREATING A USER
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

# CREATING A GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}
headers_dict = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers_dict)
# print(response.text)
# Graph is live at https://pixe.la/v1/users/strassy/graphs/graph1.html

# ADDING AN EVENT TO TRACK
today = datetime.datetime.today().strftime('%Y%m%d')

post_parameters = {
    "date": today,
    "quantity": input("How many minutes did you code today? "),
}

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=post_endpoint, json=post_parameters, headers=headers_dict)
print(response.text)

# PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
