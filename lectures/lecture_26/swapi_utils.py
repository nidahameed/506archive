import json
import requests

from functools import lru_cache
from typing import Any, Dict, Union


class CustomEncoder(json.JSONEncoder):
    """WARNING: DO NOT MODIFY.

    Extends the json module's JSONEncoder class in order to serialize
    composite class instances.

     Note: include the pylint disable comment as Windows users have
     reported issues when the default() method is called.

     Methods:
        default: overrides default method
     """

    def default(self, obj): # pylint: disable=E0202
        """Check object is provisioned with a jsonable method that is
        callable. If yes override default serialization handling.

        Parameters:
            obj (object): class instance

        Returns:
            dict: dictionary representation of the object
        """

        if hasattr(obj, 'jsonable') and callable(obj.jsonable):
            return obj.jsonable()
        else:
            return json.JSONEncoder.default(self, obj)


def convert_str_to_int(data: dict) -> dict:
    """Return select string values formatted as type int.
    Parameters:
        data (dict): key-value pairs to evaluate

    Returns:
        dict: dictionary including values, if any, that have been converted from str to int
    """

    to_int = ('diameter', 'population')

    converted: Dict[str, Any] = {}

    for key, val in data.items():
        if isinstance(val, str):
            if val.lower() == 'unknown':
                converted[key] = None
            elif key in to_int:
                converted[key] = int(val)
            else:
                converted[key] = val
        else:
            converted[key] = val

    return converted


def create_roman_numeral(value: int) -> str:
    """Return Equivalent Roman numeral equivalent of passed in Arabic numeral.

    Parameters:
        value (int): Arabic value to convert

    Returns:
        str: Roman numeral
    """

    # Tuples to the rescue
    roman = ((1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'))

    if 1 <= int(value) <= 7:
        return roman[value - 1][1]
    else:
        raise ValueError ('Argument value must be between 1 and 7')


@lru_cache(maxsize=64)
def get_swapi_resource(url: str, timeout: int = 10) -> dict:
    """Issue an HTTP GET request and return either a SWAPI resource decoded as a
    dictionary or a decoded dictionary ("the envelope") containing a list of one or more
    SWAPI resources if parameters are provided.

    Note: in order to leverage the lru_cache parameter types must be hashable. Passing in
    querystring parameters is thus disallowed. URLs that feautre querystrings must be
    constructed by the caller and passed in to this function.

    The function is wrapped with an LRU (least recently used) cache memoizing callable that
    saves up to the < maxsize > most recent calls in memory. Since a dictionary is used to
    cache results, the positional and keyword arguments to the function must be hashable.

    Parameters:
        url (str): a url that specifies the resource.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    return requests.get(url, timeout=timeout).json()


def write_custom_json(filepath: str, data: Union[dict, list]) -> None:
    """Serializes complex objects (e.g., composite class instances) as JSON
    by adding a CustomEncoder to the json.dump() call. Writes content to the
    provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict/list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, cls=CustomEncoder, ensure_ascii=False, indent=2)


def write_json(filepath: str, data: Union[dict, list]) -> None:
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)
