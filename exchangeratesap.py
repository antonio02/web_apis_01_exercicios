import requests as re
from stripe import print_respose

def main():
    url = 'https://api.exchangeratesapi.io'
    url_lastest = '{0}/lastest'.format(url)
    url_specific = '{0}/2014-01-01'.format(url)
    url_history = '{0}/history?start_at=2018-12-01&end_at=2018-12-19&symbols=USD&base=BRL'.format(url)


    response = re.get(url_specific)
    print_respose(response)

if __name__ == '__main__':
    main()