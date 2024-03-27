#!/usr/bin/env python3
"""redis exercise"""
import requests
from functools import wraps
import redis

r = redis.Redis()

def count_calls(method):
    key = f"count:{method.__qualname__}"

    @wraps(method)
    def wrapper(url):
        r.incr(key)
        return method(url)

    return wrapper

def cache_page(method):
    @wraps(method)
    def wrapper(url):
        result = r.get(url)
        if result:
            return result.decode('utf-8')
        result = method(url)
        r.setex(url, 10, result)
        return result

    return wrapper

@count_calls
@cache_page
def get_page(url: str) -> str:
    return requests.get(url).text