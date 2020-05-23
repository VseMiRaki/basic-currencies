import json
import urllib.request
import graphyte
import logging
import time

logging.getLogger().setLevel(logging.INFO)

GRAPHITE_HOST = 'graphite'
CURRENCIES = ['CAD', 'CHF', 'USD']
BASE_URL='https://api.exchangeratesapi.io/latest'
SENDER = graphyte.Sender(GRAPHITE_HOST, prefix='currencies')

def main():
    logging.info("Request: %s", BASE_URL)
    response = json.loads(urllib.request.urlopen(BASE_URL).read().decode('utf-8'))
    logging.info('Response: %s', response)
    for currency in CURRENCIES:
        SENDER.send(currency, response['rates'][currency])


if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            logging.exception("Unhandled exception")
        time.sleep(5)
