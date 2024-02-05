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

    def get(key: str, fn=None):
        """Get your data from redis db"""
        if not self._redis.exists(key):
            return None
        
        return self._redis.get(key).fn()

