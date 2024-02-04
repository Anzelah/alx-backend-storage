#!/usr/bin/env python3
"""Import your modules"""

from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient()
    db = client.logs
    col = db.nginx

    all_docs = col.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_docs = {col.count_documents({"method": m} for m in methods)}
    match_docs = col.count_documents({"method": "GET", "path": "/status"})

    print(f"{all_docs} logs")
    print("Methods:")
    for met in methods:
        print(f"\tmethod {met}: {method_docs[met]}")
    print(f"{match_docs} status check")
