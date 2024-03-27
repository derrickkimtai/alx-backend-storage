#!/usr/bin/env python3
"""redis exercise"""

import redis
from uuid import uuid4


class Cache:
    """Cache class"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """Store data in redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
