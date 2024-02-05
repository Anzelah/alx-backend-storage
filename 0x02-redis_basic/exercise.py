#!/usr/bin/env python3
"""Import your modules"""

import redis
from uuid import uuid4


class Cache:
    """Create a cache class"""
    def __init__(self):
        """Initialize the instances"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """Store your data into redis"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
