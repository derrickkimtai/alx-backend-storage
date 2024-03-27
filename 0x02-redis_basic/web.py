#!/usr/bin/env python3
"""redis exercise"""
import requests
from functools import wraps
from typing import Callable
import redis


r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count requests"""
    @wraps(method)
    def wrapper(url):
        """Wrapper function"""
        r.incr(f"count:{url}")
        return method(url)
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get the content of a web page"""
    return requests.get(url).text
