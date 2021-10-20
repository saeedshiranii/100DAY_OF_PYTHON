import os
import requests


""" first create a account """
user_endpoint = "https://pixe.la/v1/users"

my_token = os.environ.get(MY_TOKEN)
user_name = os.environ.get(USER_NAME)

parameter = {
    "token": my_token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# answer = requests.post(url=user_endpoint, json=parameter)
# print(answer.text)

""" now we are gonna pick a graph """
graph_endpoint = f"{user_endpoint}/{user_name}/graphs"
headers = {"X-USER-TOKEN": my_token}

graph_parameter = {
    "id": "graph1",
    "name": "My programing graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

# graph = requests.post(url=graph_endpoint, json=graph_parameter, headers=headers)
# print(graph.text)

""" for reach your graph search this address in your browser 'https://pixe.la/v1/users/shiranii/graphs/graph1.html'  """
