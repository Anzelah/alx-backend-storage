#!/usr/bin/env python3
"""Import your modules"""

import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Create a cache class"""
    def __init__(self):
        """Initialize the instances"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store your data into redis"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn=None) -> any:
        """Get your data from redis db"""
        if not self._redis.exists(key):
            return None 
        return self._redis.get(key)

    def get_str(self, key: str, fn=None) -> str:
        """Use correct conversion function depending on value returned"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return str(val)

    def get_int(self, key: str, fn=None) -> int:
        """Use correct conversion function depending on value returned"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return int(val)
