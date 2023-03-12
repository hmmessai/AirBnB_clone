#!/usr/bin/python3
"""Initializing elements of the models package."""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
