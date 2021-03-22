import requests
import logging

logging.basicConfig(level=logging.NOTSET)


def call_api(url, name):
    params = {
        "name": name
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_age(name):
    json = call_api("https://api.agify.io", name)
    return json["age"]


def get_gender(name):
    json = call_api("https://api.genderize.io", name)
    return json["gender"]


if __name__ == "__main__":
    name = "michael"
    age = get_age(name)
    gender = get_gender(name)
    print(name, age, gender)
