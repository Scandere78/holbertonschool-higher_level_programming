#!/usr/bin/python3
"""Defines the State class."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base
Base = declarative_base()

class State(Base):
    """Represents a state for a MySQL database."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

