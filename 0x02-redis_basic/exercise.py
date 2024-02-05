#!/usr/bin/env python3
"""Import your modules"""

import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """Decorator to count number of times method is called.
    Returns Callable: decorated method"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function to implement counting logic"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and
    outputs for a particular function"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function to implement counting logic"""
        input_key = ("{}:inputs" .format(method.__qualname__))
        output_key = ("{}:outputs" .format(method.__qualname__))
        
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper 


class Cache:
    """Create a cache class"""
    def __init__(self):
        """Initialize the instances"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store your data into redis"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
    
    def get(self, key: str, fn=None) -> any:
        """Get your data from redis db"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """Use correct conversion function depending on value returned"""
        val = self._redis.get(key)
        return val.decode("utf-8")
    
    def get_int(self, key: str) -> int:
        """Use correct conversion function depending on value returned"""
        val = self._redis.get(key)
        return int(val.decode("utf-8"))
    

def replay(method: Callable):
    """Display the history of calls of a particular function."""
    input_key = ("{}:inputs" .format(method.__qualname__))
    output_key = ("{}:outputs" .format(method.__qualname__))

    inputs = self._redis.lrange(input_key, 0, -1)
    outputs = self._redis.lrange(output_key, 0, -1)
    for i, o in zip(inputs, outputs):
        ("{} -> {}" .format(i, o))
