#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    """ Log stats """
    print(f"{mongo_collection.estimated_document_count()} logs")
    print("Methods:")
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    count = mongo_collection.count_documents(
        {"method": {"$in": METHODS}}
    )
    print(f"{count} method")
    print(mongo_collection.count_documents(
        {"method": {"$in": METHODS}, "path": "/status"}
    ), "status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(client)