#!/usr/bin/env python3
""" Update a document in Python """

def update_topics(mongo_collection, name, topics):
    """Update a document based on name and topics"""
    if mongo_collection is None:
        return None
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})