#!/usr/bin/env python3
"""Import your modules"""

from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient()
    db = client.logs
    col = db.nginx

    all_docs = col.count_documents({})
    get_docs = col.count_documents({"method": "GET"})
    post_docs = col.count_documents({"method": "POST"})
    put_docs = col.count_documents({"method": "PUT"})
    patch_docs = col.count_documents({"method": "PATCH"})
    del_docs = col.count_documents({"method": "DELETE"})
    match_docs = col.count_documents({"method": "GET", "path": "/status"})

    print("{} logs" .format(all_docs))
    print("Methods:")
    print("\tmethod GET: {}" .format(get_docs))
    print("\tmethod POST: {}" .format(post_docs))
    print("\tmethod PUT: {}" .format(put_docs))
    print("\tmethod PATCH: {}" .format(patch_docs))
    print("\tmethod DELETE: {}" .format(del_docs))
    print("{} status check" .format(match_docs))
