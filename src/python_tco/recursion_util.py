from typing import Any, Callable

import config

from stack_util import stack_size


class Recurse(Exception):
    def __init__(self, *args: Any, **kwargs: Any):
        self.args = args
        self.kwargs = kwargs


def recurse(*args: Any, **kwargs: Any):
    config.stack_depth = stack_size()
    raise Recurse(*args, **kwargs)


def tail_recursive(function: Callable[..., Any]):
    def decorated(*args: Any, **kwargs: Any):
        while True:
            try:
                return function(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated
