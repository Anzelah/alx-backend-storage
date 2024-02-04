#!/usr/bin/env python3
"""Import your modules"""

def insert_school(mongo_collection, **kwargs):
    """insert a new document in a collection based on kwargs"""
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
