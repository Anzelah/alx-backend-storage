#!/usr/bin/env python3
"""Import your modules"""


def schools_by_topic(mongo_collection, topic):
    """Return list of schools having a specific topic"""
    res = mongo_collection.find({"topics": topic})
    return res
