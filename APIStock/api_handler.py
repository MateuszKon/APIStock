import os.path
import requests
import functools
from modules.util import get_environ_file_path


# Not using decorator package because of exception generation on calling decorated function
# (which appear to have missing argument)
def api_request(function):
    @functools.wraps(function)
    def wrapper(cls, *args, **kwargs):
        # TODO: add try catch
        if cls._AUTH_KEY is None:
            cls._auth_key_file()
        return function(cls, cls._init_req(), *args, **kwargs)
    return wrapper


class ApiHandler:

    _AUTH_KEY = None

    @classmethod
    def _auth_key_file(cls):
        """
        Gets authentication key from file defined by environment variable 'APISTOCK_KEY_FILE'
        """
        try:
            # root_path is parent folder of folder containing api_handler.py
            root_path = os.path.dirname(os.path.realpath(__file__))
            root_path = os.path.dirname(root_path)
            file_path = get_environ_file_path("APISTOCK_KEY_FILE",
                                              root_path=root_path)
            with open(file_path) as f_r:
                key = f_r.readline()
                if key:
                    cls._AUTH_KEY = key
                else:
                    raise KeyError(f"File {file_path} does not contain valid authentication key!")
        except KeyError as e:
            raise Exception('Check README.md file for more information.').with_traceback(e.__traceback__)

    @classmethod
    def _init_req(cls) -> requests.Session:
        s = requests.Session()
        s.headers.update({"X-Finnhub-Token": cls._AUTH_KEY})
        return s

    @classmethod
    @api_request
    # def request_test(cls):
    def request_test(cls, request: requests.Session):
        api_url = "https://finnhub.io/api/v1/search?q=apple"
        response = request.get(api_url)
        # response = requests.patch(api_url, json={"X-Finnhub-Token": "c8acu62ad3iasddfgbi0"})
        print(response.json())


if __name__ == "__main__":
    ApiHandler.request_test()
