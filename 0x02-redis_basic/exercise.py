#!/usr/bin/env python3
"""redis exercise"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to a method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    """Cache class"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float]:
        """Get data from redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data if data else None
    
    def get_str(self, key: str) -> str:
        """Get string data from redis"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> int:
        """Get int data from redis"""
        return self.get(key, fn=int)
