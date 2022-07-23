import requests

# get a name and predict gender and age
def detector(name):
    age_dict = requests.get(f"https://api.agify.io?name={name}").json() # send request to agify and get result as a dictionry
    gender_dict = requests.get(f"https://api.genderize.io?name={name}").json() # send request to genderify and get result as a dictionry

    print(type(age_dict))

    age = age_dict["age"]
    gender = gender_dict["gender"]


    return [name, age, gender]



