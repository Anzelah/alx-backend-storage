#!/usr/bin/env python3
"""Import your modules"""


def update_topics(mongo_collection, name, topics):
    """Change topics of a school document based on name"""
    doc = mongo_collection.update_many({"name": name},
                                       {"$set": {"topics": topics}})
    return doc
