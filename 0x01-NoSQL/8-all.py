#!/usr/bin/env python3
"""Imports modules"""


def list_all(mongo_collection):
    """list all documents in a collection"""
    doc = mongo_collection.find()
    if doc:
        return doc
    return []
