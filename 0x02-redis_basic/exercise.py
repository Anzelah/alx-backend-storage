#!/usr/bin/env python3
"""Import your modules"""

import redis
from uuid import uuid4
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    def wrapper(self, *args):
        self._redis.incr(*args)
        return method(self, *args)
    return wrapper



class Cache:
    """Create a cache class"""
    def __init__(self):
        """Initialize the instances"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store your data into redis"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
    
    @count_calls
    def get(self, key: str, fn=None) -> any:
        """Get your data from redis db"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    @count_calls
    def get_str(self, key: str) -> str:
        """Use correct conversion function depending on value returned"""
        val = self._redis.get(key)
        return val.decode("utf-8")
    
    @count_calls
    def get_int(self, key: str) -> int:
        """Use correct conversion function depending on value returned"""
        val = self._redis.get(key)
        return int(val.decode("utf-8"))
