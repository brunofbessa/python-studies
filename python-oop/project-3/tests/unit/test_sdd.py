"""
Tests for SDD class
Command line: python -m pytest tests/unit/test_sdd.py
"""

import pytest 

from app.models import inventory

@pytest.fixture
def storage_values():
    return {
        'name': 'External HD', 
        'manufacturer': 'TMZHigh Tech HD', 
        'total': 10, 
        'allocated': 5, 
        'capacity_gb': 1000,
        'interface': 'ABC'
    }

@pytest.fixture
def storage(storage_values):
    return inventory.SDD(**storage_values)

def test_create_storage(storage, storage_values):
    for attr_name in storage_values:
        assert getattr(storage, attr_name) == storage_values.get(attr_name)


def test_repr(storage):
    assert storage.interface in repr(storage)
