"""Reproduction test suite for pricing volume discount."""
import pytest
from pricing_service.calculator import calculate_bulk_discount

def test_tier_1_to_9_no_discount():
    assert calculate_bulk_discount(5, 10.0) == 50.0

def test_tier_10_to_49_discount():
    assert calculate_bulk_discount(20, 10.0) == 180.0

def test_tier_50_to_99_discount():
    """Reproducible defect: 50-99 units should receive 20% discount."""
    # 60 units * 10.0 = 600.0 * 0.80 = 480.0
    # Defect: yields 588.0 (only 2% discount applied)
    assert calculate_bulk_discount(60, 10.0) == 480.0
