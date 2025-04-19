"""
Tests for HDD class
Command line: python -m pytest tests/unit/test_hdd.py
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
        'size': '2.5"', 
        'rpm': 1_000
    }

@pytest.fixture
def storage(storage_values):
    return inventory.HDD(**storage_values)

def test_create_storage(storage, storage_values):
    for attr_name in storage_values:
        assert getattr(storage, attr_name) == storage_values.get(attr_name)

@pytest.mark.parametrize(
    'size, exception', [('0"', ValueError), ('5"', ValueError)]
)
def test_create_invalid_size(size, exception, storage_values):
    storage_values['size'] = size
    with pytest.raises(exception):
        inventory.HDD(**storage_values)

@pytest.mark.parametrize(
    'rpm, exception', [(0, ValueError), ('5', TypeError)]
)
def test_create_invalid_spm(rpm, exception, storage_values):
    storage_values['rpm'] = rpm
    with pytest.raises(exception):
        inventory.HDD(**storage_values)


def test_repr(storage):
    assert storage.size in repr(storage)
    assert str(storage.rpm) in repr(storage)