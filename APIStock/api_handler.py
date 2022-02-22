import os.path
import functools

import requests
from modules.util import get_environ_file_path


class ApiHandler:

    __AUTH_KEY = None


    @classmethod
    def __auth_key_file(cls):
        """
        Gets authentication key from file defined by environment variable 'APISTOCK_KEY_FILE'
        """
        try:
            # root_path is parent folder of folder containing api_handler.py
            file_path = get_environ_file_path("APISTOCK_KEY_FILE",
                                              root_path=os.path.dirname(os.path.realpath(__file__)).dirname)
            with open(file_path) as f_r:
                key = f_r.readline()
                print(key)
                if key:
                    cls.__AUTH_KEY = key
                else:
                    raise KeyError(f"File {file_path} does not contain valid authentication key!")
        except KeyError as e:
            raise Exception('Check README.md file for more information.').with_traceback(e.__traceback__)

    @classmethod
    def request_test(cls, request: requests.Session):
        api_url = "https://finnhub.io/api/v1/search?q=apple"
        response = request.get(api_url, )
        # response = requests.patch(api_url, json={"X-Finnhub-Token": "c8acu62ad3iasddfgbi0"})
        print(response.json())

    @classmethod
    def init_req(cls):
        s = requests.Session()
        s.headers.update({"X-Finnhub-Token": "c8acu62ad3iasddfgbi0"})
        return s

    @staticmethod
    def api_request(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            # TODO: how wrap classmethod?
            pass
            ret_value = function(*args, **kwargs)
            return ret_value
        return wrapper
