# common
This module contains the abstract class Common, that defines all the attributes and methods all classes must have

## Uses/Requires/Imports:
- abc
- datetime
- uuid

## Attributes:
### Private instance attributes
- ``oid``: object id, created by ``uuid.uuid4()``
- ``created_at``: object creation time, set by ``datetime.utcnow()``
- ``updated_at``: object creation time, set by ``datetime.utcnow()``

## Methods:
### Getters:
- [X] oid
- [X] created_at
- [X] updated_at
### Setters:
- [X] oid
- [X] created_at
- [X] updated_at
### Behaviors:
- ``__setattr__()``: Whenever an attribute changes, updated_at is updated automatically
### Abstract:
- ``to_dict``: Returns a dictionary representation for the instance;