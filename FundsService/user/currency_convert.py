from requests import post, get
from os import getenv


def convert_funds(currency: str, amount: float):

    url = "https://community-neutrino-currency-conversion.p.rapidapi.com/convert/"

    payload = {
        "from-value": str(amount),
        "from-type": "UAH",
        "to-type": currency
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "dd25f2d9aamshf5fc1471b40eadcp1d03a6jsna32eccbce5c3",
        "X-RapidAPI-Host": getenv('API_HOST')
    }

    response = post(url, data=payload, headers=headers).json()

    print(response)

    if 'valid' in response and response['valid'] is True:
        return response['result-float']
    else:
        return None