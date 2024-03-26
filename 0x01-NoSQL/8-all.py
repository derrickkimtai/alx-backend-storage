#!/usr/bin/env python3

def list_all(mongo_collection):
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({}))