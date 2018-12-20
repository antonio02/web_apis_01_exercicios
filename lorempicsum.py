import requests as re
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

from stripe import print_respose


def main():
    url = 'https://picsum.photos'
    url_grey = '{0}/g/1280/720/?random'.format(url)
    url_blur = '{0}/1280/720/?blur'.format(url)
    url_list = '{0}/list'.format(url)

    response = re.get(url_blur)
    response_list = re.get(url_list)

    print_respose(response_list)

    im = Image.open(BytesIO(response.content))

    plt.imshow(im)
    plt.show()

if __name__ == '__main__':
    main()