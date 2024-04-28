#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection based on keyword arguments.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Keyword arguments representing the fields and values of the new document.

    Returns:
        The new _id of the inserted document.
    """
    new_doc = kwargs
    result = mongo_collection.insert_one(new_doc)
    return result.inserted_id
