import time
import uuid

from httprunner import __version__

def gen_random_request_id():
    request_id = str(uuid.uuid4())
    print(request_id)
    return request_id

def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)
