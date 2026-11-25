"""Inventory service stock management."""

_STOCK = {
    "SKU-100": 50,
    "SKU-200": 10,
}

def reserve_inventory(sku: str, quantity: int) -> dict:
    """Reserve inventory for a given SKU.
    
    Returns:
        dict: {"status": "CONFIRMED", "reserved": quantity, "sku": sku} on success,
              {"status": "OUT_OF_STOCK", "reserved": 0, "sku": sku} on failure.
    """
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    available = _STOCK.get(sku, 0)
    if available >= quantity:
        _STOCK[sku] = available - quantity
        return {"status": "CONFIRMED", "reserved": quantity, "sku": sku}
    return {"status": "OUT_OF_STOCK", "reserved": 0, "sku": sku}
