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
        #create keys for output and input lists to be used
        input_key = ("{}:inputs" .format(method.__qualname__))
        output_key = ("{}:outputs" .format(method.__qualname__))
        
        #ensure arguments when method is called are str for redis
        input_params = str(args)

        #add input parameters to our created list everytime function is called
        self._redis.rpush(input_key, input_params)

        #execute the wrapped function to get output of our input
        output = method(self, *args, **kwds)

        #serialize this as well before adding to our created list
        output_serialize = str(output)
        self._redis.rpush(output_key, output_serialize)
        
        #return previous output from when our wrapped function executed
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
