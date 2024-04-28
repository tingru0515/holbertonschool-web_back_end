#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection"""
def list_all(mongo_collection):
    """
    List all documents in a collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        List of documents in the collection.
        Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find())
