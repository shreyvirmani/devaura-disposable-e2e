"""Reproduction test suite for math service calculator."""
import pytest
from math_service.calculator import calculate_discount

def test_standard_discount():
    assert calculate_discount(100.0, "standard") == 95.0

def test_premium_discount():
    assert calculate_discount(100.0, "premium") == 85.0

def test_enterprise_discount_failure():
    """Reproducible defect: Enterprise customers should receive 25% discount."""
    # Defect: Returns 95.0 instead of 75.0
    assert calculate_discount(100.0, "enterprise") == 75.0
