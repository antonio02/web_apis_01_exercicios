import requests as re
import json

def main():
    cep = '64218100'
    url = "https://viacep.com.br/ws/{cep}/json/"
    url = url.format(cep=cep)
    response = re.get(url).json()
    print(format_json(response))

    print("Logradouro: %s \nBairro: %s \nLocalidade: % s \nUF: % s" %
    (response['logradouro'],
     response['bairro'],
     response['localidade'], response['uf']))

    # key = ''
    # localizacao = "Avenida frei serafim"
    # url ='https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (localizacao, key)
    # json = re.get(url).json()
    # print(format_json(json))
    # latitude = json['results'][0]['geometry']['location']['lat']
    # longitude = json['results'][0]['geometry']['location']['lng']

    url = 'https://jsonplaceholder.typicode.com/todos/'
    dados = {
        "userId": 1,
        "title": 'Prepare class notes',
        "completed": False
    }
    response = re.post(url, data=dados).json()
    print(format_json(response))
    response = re.delete(url + '210')
    # 404
    print(response)

def format_json(dict_json):
    return json.dumps(dict_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()