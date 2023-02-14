import json

def handle(data):

    data = json.loads(data)
    products = data["products"]
    result = []
    page = []
    products_list = []
    for i in range(len(products)):
        product = products[i]
        if (i+1)%9 == 0 or (i==len(products)-1):
            page.append(product)
            result.append(page)
            page = []
        else:
            page.append(product)
            

    return json.dumps({"result":result})
