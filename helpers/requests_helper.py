import requests
import logging


def request_helper(req_url):
    try:
        logging.info("running WS request " + req_url)
        req = requests.get(req_url)
        return req
    except requests.exceptions.ConnectionError:
        raise ConnectionError("connection error , please check server")
    except requests.exceptions.HTTPError:
        logging.error("http err")
        raise

