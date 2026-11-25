"""Reproduction test suite for order pipeline checkout."""
import pytest
from order_pipeline.checkout import process_checkout

def test_checkout_reservation_flow():
    """Reproducible defect: Argument transposition causes TypeError in reservation."""
    result = process_checkout(order_id="ORD-1", sku="SKU-100", quantity=2)
    assert result["status"] == "COMPLETED"
    assert result["order_id"] == "ORD-1"
