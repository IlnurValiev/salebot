import json

def handle(data):

    data = json.loads(data)
    return data['name']
