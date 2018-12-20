import requests as re
from slide_exercicios import format_json

def main():
    key = 'sk_test_GUSVwwYRlkkMPyuPIsm3x4dZ'
    url = 'https://api.stripe.com/v1'
    headers = {'Authorization': 'Bearer {0}'.format(key)}

    # customers(url, headers)
    # balance(url, headers)
    # charges(url, headers)
    # products(url, headers)
    # skus(url, headers)
    orders(url, headers)



def customers(url, headers):
    customer_url = '{0}/customers'.format(url)

    data = {
        'description': 'Cliente com cartão',
        'email': 'cartao@teste.com',
        'source': 'tok_visa'
    }

    response = re.post(customer_url, headers=headers, data=data)
    print_respose(response)

    # get_customer_url = '{0}/{1}'.format(url, response.json()['id'])
    # response = re.delete(get_customer_url, headers=headers).json()

    response = re.get(customer_url, headers=headers)
    print_respose(response)


def balance(url, headers):
    balance_url = '{0}/balance'.format(url)
    response = re.get(balance_url, headers=headers)

    print_respose(response)


def charges(url, headers):
    charges_url = '{0}/charges'.format(url)

    data = {
        'amount': 2000,
        'currency': 'brl',
        'customer': 'cus_EBfsv2VDbNKHv9',
        'description': "Cobra cobra a cobra"
    }

    response = re.post(charges_url, headers=headers, data=data)
    print_respose(response)


def products(url, headers):
    products_url = '{0}/products'.format(url)

    data = {
        'name': 'Camisa',
        'type': 'good', # good or service
        'description': 'Camisa de algodão',
        'attributes[]': {"tamanho", "genero"},
    }

    response = re.post(products_url, headers=headers, data=data)
    print_respose(response)


def skus(url, headers):
    skus_url = '{0}/skus'.format(url)

    data = {
        'attributes[tamanho]': 'G',
        'attributes[genero]': 'M',
        'price': 50,
        'currency': 'brl',
        'inventory[type]': 'finite',
        'inventory[quantity]': 10,
        'product': 'prod_EBg4kWy7XglgzQ',
    }

    response = re.post(skus_url, headers=headers, data=data)
    print_respose(response)


def orders(url, headers):
    orders_url = '{0}/orders'.format(url)

    data = {
        'items[][type]': 'sku',
        'items[][parent]': 'sku_EBgDkpmdMBhlZf',
        'currency': 'brl',
        'customer': 'cus_EBfsv2VDbNKHv9',
        'shipping[name]': 'Jose',
        'shipping[address][city]': 'Teresina',
        'shipping[address][state]': 'PI',
        'shipping[address][country]': 'BR',
        'shipping[address][postal_code]': '64000-000',
        'shipping[address][line1]': 'Av. Miguel Rosa',
    }

    response = re.post(orders_url, headers=headers, data=data)
    print_respose(response)


def print_respose(response):
    print(response.status_code, format_json(response.json()))



if __name__ == '__main__':
    main()