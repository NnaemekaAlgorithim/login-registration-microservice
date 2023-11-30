#!/usr/bin/python3
"""Instantiates a storage object."""
from models.engines.db_engine import DBStorage


storage = DBStorage()
storage.reload()
