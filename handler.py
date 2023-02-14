import json

def handle(data):

    data = json.loads(data)
    products = data["products"]
    prices = data["prices"]
    prices_sale = data["prices_sale"]
    category = data["category"]
    subcategory = data["subcategory"]
    coupons = data["coupons"]
    result = []
    page = []
    products_list = []
    for i in range(len(products)):
        prices_sale[i] = prices_sale[i].replace(',','.')
        prices_sale[i] = float(prices_sale[i])
        if coupons:
            for k in range(len(coupons)):
                coupon = str(coupons[k]).split(';')
                typE = coupon[0]
                obj = coupon[1]
                sale = str(coupon[2])
                sale = sale.replace(',','.')
                sale = int(sale)
                if typE == 'категория':
                    if category == obj:
                        prices_sale[i] -= prices_sale[i]*sale/100
                elif typE == 'подкатегория':
                    if subcategory == obj:
                        prices_sale[i] -= prices_sale[i]*sale/100
                elif typE == 'товар':
                    if products[i] == obj:
                        prices_sale[i] -= prices_sale[i]*sale/100
                elif typE == 'все товары':
                    prices_sale[i] -= prices_sale[i]*sale/100

        prices_sale[i] = round(prices_sale[i],1)
        
        if int(prices[i]) == int(prices_sale[i]):
            product = str(products[i]) + ' - '+str(prices_sale[i]) + ' шек.'
            product1 = str(products[i])
        else:
            product = str(products[i]) + ' - '+str(prices_sale[i]) + ' (без скидки '+ str(prices[i])+') шек.'
            product1 = str(products[i]) + ' (без скидки '+ str(prices[i])+')
        
        products_list.append([product1,(prices_sale[i])])         
    
        if (i+1)%9 == 0 or (i==len(products)-1):
            page.append(product)
            result.append(page)
            page = []
        else:
            page.append(product)
            

    return json.dumps({"result":result,"products_list":products_list})
