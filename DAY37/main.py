from datetime import datetime
import requests


""" first create a account """
user_endpoint = "https://pixe.la/v1/users"

my_token = ""
user_name = ""

parameter = {
    "token": my_token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#answer = requests.post(url=user_endpoint, json=parameter)
#print(answer.text)

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

#graph = requests.post(url=graph_endpoint, json=graph_parameter, headers=headers)
#print(graph.text)

""" for reach your graph search this address in your browser 'https://pixe.la/v1/users/shiranii/graphs/graph1.html'  """


today = datetime.now()
print(today.strftime("%Y%m%d"))
draw_params= {
            "date": today.strftime("%Y%m%d"),
            "quantity":"40000"}
        
draw_url = F"{user_endpoint}/{user_name}/graphs/graph1"

headers={'X-USER-TOKEN':my_token}

#graph = requests.post(url=draw_url, json=draw_params, headers=headers)
#print(graph.text)